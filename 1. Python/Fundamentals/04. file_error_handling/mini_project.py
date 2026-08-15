def saveStudent(name, marks):
    with open("Details.txt", "a") as file:
        file.write(f"{name},{marks}\n")

def showDetails():
    try:
        with open("Details.txt", "r") as file:
            data = file.readlines()

        if not data:
            print("No student records found")
            return
        
        print("\n---Student Records---")
        for line in data:
            name, marks = line.strip().split(",")
            print(f"Name: {name}, Marks: {marks}")

    except FileNotFoundError:
        print("File not found")


def findTopper():
    with open("Details.txt", "r") as file:
        data = file.readlines()

    if not data:
        print("No student records found")
        return
    
    topper = ""
    highest_marks = -1

    for line in data:
        name, marks = line.strip().split(",")
        marks = int(marks)
        if marks > highest_marks:
            highest_marks = marks
            topper = name

    print(f"\nTopper: {topper}, Marks: {highest_marks}")


def menu():
    while True:
        print("\n---Student Records Storage System---")
        print("1.Save Student Details")
        print("2.Show Student Details")
        print("3.Find Topper")
        print("4.Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            marks = input("Enter student marks: ")
            saveStudent(name, marks)

        elif choice == "2":
            showDetails()

        elif choice == "3":
            findTopper()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

menu()