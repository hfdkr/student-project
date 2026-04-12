# Create an empty dictionary
students = {}
while True:
    name = input("Enter student name (or type 'stop' to finish): ")
    
    if name.lower() == 'stop':
        break
    
    try:
        note = float(input(f"Enter grade for {name}: "))
        students[name] = note
    except ValueError:
        print("Please enter a valid number for the grade.")

# Display the dictionary
print("\nStudent Dictionary:")
for name, note in students.items():
    print(f"{name}: {note}")
