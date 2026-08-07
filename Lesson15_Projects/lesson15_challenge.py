student_grades = {

    'Trystan': 90,
    'Alice': 87,
    'Braxton': 91,
    'Bella': 89

}

def view_grades():

    print()
    print('==== Current Grades ====')
    print()

    for student, grade in student_grades.items():
        print(student + ':', grade)

    print()

def update_grade():

    student_name = input('Which student? ')

    if student_name not in student_grades:
        print('Not a student!')

    while True:

        try:

            student_grade = int(input('What is their new grade? '))
            print('Valid Grade!')

            break

        except ValueError:
            print('Invalid Grade!')

    if student_name in student_grades:
        student_grades[student_name] = student_grade
        print('Grade Updated!')

    view_grades()

def add_student_grade():

    student_name = input('What is the students name? ')

    while True:

        try:

            student_grade = int(input('What is the students grade? '))
            print('Valid Grade!')

            break

        except ValueError:
            print('Invalid Grade!')

    if student_name not in student_grades:
        student_grades[student_name] = student_grade

    print('Student Added!')

    view_grades()

def delete_student():

    student_name = input('What is the students name? ')

    if student_name in student_grades:

        del student_grades[student_name]
        print('Student Deleted!')

    else:
        print('Student already doesnt exist!')

    view_grades()

def save_student_grades():

    with open('Student_Grades.txt', 'w') as file:

        for student, grade in student_grades.items():

            file.write(student + ':' + str(grade) + '\n')

    print('Grades Saved!')

while True:

    print('==== Student Grade Manager ====')

    print('1. View Grades')
    print('2. Update Grades')
    print('3. Add Grade')
    print('4. Delete Student')
    print('5. Save Grades')
    print('6. Exit')

    choice = input('Choose a option: ')

    if choice == '1':
        view_grades()

    if choice == '2':
        update_grade()

    if choice == '3':
        add_student_grade()

    if choice == '4':
        delete_student()

    if choice == '5':
        save_student_grades()

    if choice == '6':
        print('Goodbye!')

        break