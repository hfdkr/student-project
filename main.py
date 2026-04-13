# ==============================
# Gestion des étudiants - version améliorée
# ==============================

FICHIER = "etudiants.txt"
etudiants = []


# -----------------------------
# Sauvegarder dans un fichier texte
# -----------------------------
def sauvegarder_dans_fichier():
    try:
        with open(FICHIER, "w", encoding="utf-8") as f:
            for e in etudiants:
                ligne = f"{e['nom']};{e['age']};{e['note']}\n"
                f.write(ligne)
        print(" Données sauvegardées avec succès.")
    except Exception as e:
        print(" Erreur lors de la sauvegarde :", e)


# -----------------------------
# Charger depuis un fichier texte
# -----------------------------
def charger_depuis_fichier():
    global etudiants
    try:
        with open(FICHIER, "r", encoding="utf-8") as f:
            etudiants = []
            for ligne in f:
                ligne = ligne.strip()
                if ligne:
                    nom, age, note = ligne.split(";")
                    etudiants.append({
                        "nom": nom,
                        "age": int(age),
                        "note": float(note)
                    })
        print(" Données chargées avec succès.")
    except FileNotFoundError:
        print(" Aucun fichier trouvé. Une nouvelle liste sera utilisée.")
    except Exception as e:
        print(" Erreur lors du chargement :", e)


# -----------------------------
# Ajouter un étudiant
# -----------------------------
def ajouter_etudiant():
    try:
        nom = input("Nom : ").strip()
        age = int(input("Age : "))
        note = float(input("Note : "))

        if not nom:
            print(" Le nom ne doit pas être vide.")
            return

        etudiant = {
            "nom": nom,
            "age": age,
            "note": note
        }

        etudiants.append(etudiant)
        print(" Étudiant ajouté avec succès !")

    except ValueError:
        print(" Erreur dans la saisie !")


# -----------------------------
# Afficher les étudiants
# -----------------------------
def afficher_etudiants():
    if len(etudiants) == 0:
        print(" Aucun étudiant trouvé.")
    else:
        print("\nListe des étudiants :")
        for i, e in enumerate(etudiants, start=1):
            print(f"{i} - Nom: {e['nom']} | Age: {e['age']} | Note: {e['note']}")


# -----------------------------
# Rechercher un étudiant
# -----------------------------
def rechercher_etudiant():
    nom = input("Entrer le nom à rechercher : ").strip()
    trouve = False

    for e in etudiants:
        if e["nom"].lower() == nom.lower():
            print(" Étudiant trouvé :", e)
            trouve = True

    if not trouve:
        print(" Étudiant non trouvé.")


# -----------------------------
# Modifier un étudiant
# -----------------------------
def modifier_etudiant():
    nom = input("Nom de l'étudiant à modifier : ").strip()

    for e in etudiants:
        if e["nom"].lower() == nom.lower():
            try:
                e["age"] = int(input("Nouveau age : "))
                e["note"] = float(input("Nouvelle note : "))
                print(" Étudiant modifié !")
                return
            except ValueError:
                print(" Erreur de saisie.")
                return

    print(" Étudiant non trouvé.")


# -----------------------------
# Supprimer un étudiant
# -----------------------------
def supprimer_etudiant():
    nom = input("Nom de l'étudiant à supprimer : ").strip()

    for e in etudiants:
        if e["nom"].lower() == nom.lower():
            etudiants.remove(e)
            print(" Étudiant supprimé !")
            return

    print(" Étudiant non trouvé.")


# -----------------------------
# Trier les étudiants
# -----------------------------
def trier_etudiants():
    if len(etudiants) == 0:
        print(" Aucun étudiant à trier.")
        return

    print("\n--- Tri des étudiants ---")
    print("1. Trier par nom")
    print("2. Trier par age")
    print("3. Trier par note")
    choix = input("Votre choix : ")

    if choix == "1":
        etudiants.sort(key=lambda e: e["nom"].lower())
        print(" Étudiants triés par nom.")
    elif choix == "2":
        etudiants.sort(key=lambda e: e["age"])
        print(" Étudiants triés par age.")
    elif choix == "3":
        etudiants.sort(key=lambda e: e["note"])
        print(" Étudiants triés par note.")
    else:
        print(" Choix invalide.")


# -----------------------------
# Calcul de statistiques simples
# -----------------------------
def statistiques_etudiants():
    if len(etudiants) == 0:
        print(" Aucun étudiant disponible pour les statistiques.")
        return

    total = len(etudiants)
    somme_notes = sum(e["note"] for e in etudiants)
    moyenne = somme_notes / total
    note_max = max(e["note"] for e in etudiants)
    note_min = min(e["note"] for e in etudiants)

    print("\n--- Statistiques ---")
    print("Nombre total d'étudiants :", total)
    print("Moyenne des notes :", round(moyenne, 2))
    print("Note maximale :", note_max)
    print("Note minimale :", note_min)


# -----------------------------
# MENU PRINCIPAL
# -----------------------------
def menu():
    charger_depuis_fichier()

    while True:
        print("\n===== Gestion des étudiants =====")
        print("1. Ajouter un étudiant")
        print("2. Afficher les étudiants")
        print("3. Rechercher un étudiant")
        print("4. Modifier un étudiant")
        print("5. Supprimer un étudiant")
        print("6. Sauvegarder dans un fichier")
        print("7. Charger depuis le fichier")
        print("8. Trier les étudiants")
        print("9. Afficher les statistiques")
        print("0. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            ajouter_etudiant()
        elif choix == "2":
            afficher_etudiants()
        elif choix == "3":
            rechercher_etudiant()
        elif choix == "4":
            modifier_etudiant()
        elif choix == "5":
            supprimer_etudiant()
        elif choix == "6":
            sauvegarder_dans_fichier()
        elif choix == "7":
            charger_depuis_fichier()
        elif choix == "8":
            trier_etudiants()
        elif choix == "9":
            statistiques_etudiants()
        elif choix == "0":
            sauvegarder_dans_fichier()
            print(" Au revoir !")
            break
        else:
            print(" Choix invalide.")


# Lancement du programme
menu()