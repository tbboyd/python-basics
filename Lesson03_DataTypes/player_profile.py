name = input('What is your name? ')
age = int(input('How old are you? '))
gpa = float(input('What is your gpa? '))
student = input('Are you a student? (yes/no): ')

is_student = student.lower() == 'yes'

print()
print('==== Player Profile =====')
print('Name: ', name)
print('Age: ', age)
print('gpa: ', gpa)
print('Student: ', is_student)
