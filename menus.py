from teacher import Teacher
from grade import Grade

students = []# creates an empty list to hold student objects
teachers = []# creates an empty list to hold teacher objects

def addStudents():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        type = input('Enter type (Student or Teacher): ')
        course = input('Enter Course: ')
        year = input('Enter year: ')
        section = input('Enter section: ')
        print('----------------------------')
        filipino = input('Grade filipino: ')
        math = input('Grade math: ')
        science = input('Grade science: ')
        english = input('Grade english: ')

        stud = Grade(filipino, math, science, english) # Create a Grade object with the given grades
        # Assign values to the Grade object's attributes
        stud.id = id
        stud.last_name = lastName
        stud.first_name = firstName
        stud.middle_name = middleName
        stud.type = type
        stud.course = course
        stud.year = year
        stud.section = section

        students.append(stud)  # adds the Grade object to the students list
        print('Student added successfully!')
        print()
        ans = input('Enter another? [y/n]: ')

 # Break the loop if the user enters 'n'
        if (ans != 'y'):
            break

    menu() # calls the menu function

def addTeachers():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        type = input('Enter type (Student or Teacher): ')
        position = input('Enter position: ')
        department = input('Enter department: ')
        college = input('Enter College: ')

        # Create a Load object with the given subject, hours, and units
        teach = Teacher(department,position,college) 
        # Assign values to the Load object's attributes
        teach.id = id
        teach.last_name = lastName
        teach.first_name = firstName
        teach.middle_name = middleName
        teach.type = type
        teach.college = college
        teach.department =  department
        teach.position = position

        teachers.append(teach) # adds the Load object to the teachers
        print('Teacher added successfully!')
        print()
        ans = input('Enter another? [y/n]: ')

        # Call the menu function after the loop finishes
        if (ans != 'y'):
            break

    menu()
    
def deleteRecord():  # Prompt the user for the index of the record to delete
    global record_type
    choice = input('Enter index of record to delete (enter "all" to delete all records): ')
    if (record_type == 'S'): # Check if the record type is a student record
        if choice.lower() == 'all':  # If the user entered 'all', clear all the student records
            students.clear()
        else: # Otherwise, remove the student record at the specified index
            i = int(choice)
            students.pop(i)
    elif (record_type == 'T'):# Check if the record type is a teacher record
        if choice.lower() == 'all':# If the user entered 'all', clear all the teacher records
            teachers.clear()
        else:# Otherwise, remove the teacher record at the specified index
            i = int(choice)
            teachers.pop(i)

    menu()# Call the menu function to display the main men  


def searchRecord():
    global record_type
    choice = input('Enter index of record to search: ')# Prompt the user for the index of the record to search
    if (record_type == 'S'):# Check if the record type is a student record
        i = int(choice)
         # Print the details of the student record at the specified index
        print(f'{i} \t | {students[i].id} | \t {students[i].getName()} \t | {students[i].getStud()} \t | {students[i].getAverage()}')
         # Check if the record type is a teacher record
    elif (record_type == 'T'):
        i = int(choice)
        # Print the details of the teacher record at the specified index
        print(f'{i} \t | {teachers[i].id()} | \t {teachers[i].getName()} \t | {teachers[i].getDept()} \t | {teachers[i].getPosition()}')

    menu()


# Modify the displayRecords function to take the record type as a parameter
def displayRecords(record_type):
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    # Loop through each student record and print their details
    if record_type == 'S':
        for s in students:
            print(f'{i} \t | {students[i].id}  \t | {s.getName()} \t | {s.getStud()} \t | {s.getAverage()}')
            i += 1
    # Loop through each teacher record and print their details
    elif record_type == 'T':
        for t in teachers:
            print(f'{i} \t | {t.getName()} \t | {t.getPosition()} \t | {t.getDept()}  \t | {t.getCollege()}  ')
            i += 1  
    # Loop through each record and print their details
    elif record_type == 'A':
        for s in students:
            print(f'{i} \t | {students[i].id}  \t | {s.getName()} \t | {s.getStud()} \t | {s.getAverage()}')
            i += 1
        for t in teachers:
            print(f'{i} \t | {t.getName()}  \t | {t.getPosition()} \t | {t.getDept()}\t | {t.getCollege()}')
            i += 1
    print()

# Define a function called 'menu'
def menu():
    print()
    print('Welcome to the Student/Teacher Record System!')
    print('Please select an option:')
    print('1. Add Student')
    print('2. Add Teacher')
    print('3. Delete Record')
    print('4. Search Record')
    print('5. Display Records (S for student, T for teacher, A for all)')
    print('6. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        addStudents()
    elif choice == '2':
        addTeachers()
    elif choice == '3':
        record_type = input('Enter record type (S for student, T for teacher): ')
        deleteRecord(record_type)
    elif choice == '4':
        record_type = input('Enter record type (S for student, T for teacher): ')
        searchRecord(record_type)
    elif choice == '5':
        record_type = input('Enter record type (S for student, T for teacher, A for all): ')
        displayRecords(record_type)
    elif choice == '6':
        print('Goodbye!')
        return
    else:
        print('Invalid choice. Please try again.')
    menu()

    print()

menu()
