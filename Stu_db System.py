
import os
students=[]
FILE_NAME = "students.txt"

def load_data():
    global students
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                students = []

                for line in file:
                    line = line.strip()

                    if line:
                        parts = line.split(',') 
                        student = {
                            'roll_no':int(parts[0]),
                            'name': parts[1],
                            'marks' : float(parts[2])
                        }
                        students.append(student)
            print(f"{len(students)} students loaded successfully!\n")
        else:
            print("No existing data file found. Starting Fresh!\n") 
    except Exception as e:
        print(f"Error loading data:{e}\n")                     

def save_data():
    try:
        with open(FILE_NAME, 'w') as file:
            for  student in students:
                line = f"{student['roll_no']},{student['name']}, {student['marks']}\n"
                file.write(line)
        print("Data saved successfully!\n")
    except Exception as e:
        print(f"Error Saving Data:{e}\n")            

def add_student():
    print("\n ADD NEW STUDENT")
    print("-" * 40)
    try:
        roll_no = int(input("enter roll number:"))
        for student in students:
            if student['roll_no'] == roll_no:
                print("Role number alredy  exists!\n")
                return 
        name = input("enter name: ")
        marks = float(input("enter marks(0-100):"))
        #validation
        if marks < 0 or marks>100:
            print("marks should be between 0 to 100!\n")
            return
        student = {
            'roll_no' :roll_no,
            'name' : name,
            'marks' : marks
            }
        students.append(student)
        save_data()
        print(f" Student {name} added successfully!\n")

    except ValueError:
        print("invalid input! please enter numbers correctly.\n")
    except Exception as e:
        print(f"Error:{e}\n")        



def view_all_students():
    print("\n ALL STUDENTS")
    print("=" *60)

    if not students:
        print("no students found!\n")
        return
    print(f"{'Roll No':<10} {'Name':<20} {'Marks':<10} {'Grade':<10}")
    print("_"*60)

    for student in students:
        grade = calculate_grade(student['marks'])
        print(f"{student['roll_no']:<10} {student['name']:<20} {student['marks']:<10.2f} {grade:<10}")

    print("=" *60)
    print(f"Total Students:{len(students)}\n")

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def search_students():
    print("\n SEARCH STUDENT")
    print("_" * 40)
    try:
        roll_no = int(input("Enter Roll Number to search:"))

        for student in students:
            if student['roll_no'] == roll_no:
                print("\n Student Found!")
                print(f"Roll No: {student['roll_no']}")
                print(f"Name: {student['name']}")
                print(f"Marks: {student['marks']}")
                print(f"Grade:{calculate_grade(student['marks'])}\n")
                return
        print("Student Not Found!\n") 
    except ValueError:
        print("Invalid roll number!\n")       

def update_student():
    print("\n UPDATE STUDENT")
    print("_"*40)
    try:
        roll_no = int(input("Enter Roll number to update:"))

        for student in students:
            if student['roll_no'] == roll_no:
                print(f"\nCurrent Name : {student['name']}")
                print(f"Current Marks:{student['marks']}")

                new_name = input("\n Enter new name(press enter to keep current):")
                new_marks = input("Enter new marks(press enter to keep current):")

                if new_name:
                    student['name'] = new_name

                if new_marks:
                    student['marks'] = float(new_marks) 

                    if student['marks'] < 0 or student['marks']>100:
                        print("marks should be between 0 to 100!\n")
                        return
                save_data()    
                print("Student Updated Successfully!\n")
                return
        print("Student not found") 
    except ValueError:
        print("invalid data")   
def delete_student():
    print("\n DELETE STUDENT")
    print("_"*40)

    try:
        roll_no = int(input("Enter Roll Number to delete:"))
        for i, student in enumerate(students):
            if student['roll_no'] == roll_no:
                print(f"\n Student:{student['name']} (Roll No:{roll_no})")
                confirm = input("Are you sure you want to delete? (yes/no):")

                if confirm.lower() == 'yes':
                    students.pop(i)
                    save_data()
                    print("Student delete successfully!\n")
                else:
                    print("Deleted Cancelled\n")
                return
        print("Student not found!\n")
    except ValueError:
        print("invalid roll number!\n")                
def show_menu():
    print("\n" + "=" * 50)
    print("STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Students")
    print("4. Update Student")
    print("5. Delete Students")
    print("6. Exit")
    print("=" * 50)

    
def main():
    print("\n Welcome To Student Management System!")
    load_data()
    while True:
        show_menu()
        try:
            choice = input("\n Enter Your choice(1-6):")
            if choice == '1':
                add_student()
            elif choice == '2':
                view_all_students()
            elif choice == '3':
                search_students()
            elif choice == '4':
                update_student()
            elif choice == '5':
                delete_student()
            elif choice == '6':
                print("\n Thankyou for using Student management system!")
                break
            else:
                print("Invalid choice")
        except KeyboardInterrupt:
            print("\n\n Program interrupted by user!")        
            save_data()
            break
        except Exception as e:
            print(f"An error occurred:{e}\n")
if __name__ == "__main__":
    main()
            