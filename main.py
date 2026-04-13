# Liste principale des étudiants
etudiants = []

# -----------------------------
# Fonction pour ajouter un étudiant
# -----------------------------
def ajouter_etudiant():
    try:
        nom = input("Nom : ")
        age = int(input("Age : "))
        note = float(input("Note : "))

        etudiant = {
            "nom": nom,
            "age": age,
            "note": note
        }

        etudiants.append(etudiant)
        print(" Étudiant ajouté avec succès !")

    except:
        print(" Erreur dans la saisie !")


# -----------------------------
# Fonction pour afficher les étudiants
# -----------------------------
def afficher_etudiants():
    if len(etudiants) == 0:
        print(" Aucun étudiant trouvé.")
    else:
        print("\n Liste des étudiants :")
        for i, e in enumerate(etudiants):
            print(i, "- Nom:", e["nom"], "| Age:", e["age"], "| Note:", e["note"])


# -----------------------------
# Fonction pour rechercher un étudiant
# -----------------------------
def rechercher_etudiant():
    nom = input("Entrer le nom à rechercher : ")
    trouve = False

    for e in etudiants:
        if e["nom"].lower() == nom.lower():
            print(" Étudiant trouvé :", e)
            trouve = True

    if not trouve:
        print(" Étudiant non trouvé.")


# -----------------------------
# Fonction pour modifier un étudiant
# -----------------------------
def modifier_etudiant():
    nom = input("Nom de l'étudiant à modifier : ")

    for e in etudiants:
        if e["nom"].lower() == nom.lower():
            try:
                e["age"] = int(input("Nouveau age : "))
                e["note"] = float(input("Nouvelle note : "))
                print(" Étudiant modifié !")
                return
            except:
                print(" Erreur de saisie.")
                return

    print(" Étudiant non trouvé.")


# -----------------------------
# Fonction pour supprimer un étudiant
# -----------------------------
def supprimer_etudiant():
    nom = input("Nom de l'étudiant à supprimer : ")

    for e in etudiants:
        if e["nom"].lower() == nom.lower():
            etudiants.remove(e)
            print(" Étudiant supprimé !")
            return

    print(" Étudiant non trouvé.")


# -----------------------------
# MENU PRINCIPAL
# -----------------------------
def menu():
    while True:
        print("\n=====  Gestion des étudiants =====")
        print("1. Ajouter un étudiant")
        print("2. Afficher les étudiants")
        print("3. Rechercher un étudiant")
        print("4. Modifier un étudiant")
        print("5. Supprimer un étudiant")
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
        elif choix == "0":
            print(" Au revoir !")
            break
        else:
            print(" Choix invalide.")


# Lancement du programme
menu()