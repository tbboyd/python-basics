## ==== Challenge 1 ====

file = open('favorite_quote.txt', 'w')

file.write('Your mom')

file.close()

file = open('favorite_quote.txt', 'r')

content = file.read()

print(content)

# ==== Challenge 2 ====

print("==== Student Grade Recorder ====")
print()

# Ask the user for information
student_name = input("Enter student name: ")
student_grade = input("Enter student grade: ")

# Save the information to the file
with open("grades.txt", "a") as file:
    file.write(student_name + " - " + student_grade + "\n")

print()
print("Student saved successfully!")
print()

# Display all students currently in the file
print("==== Current Grade Book ====")

with open("grades.txt", "r") as file:
    for line in file:
        print(line.strip())

print()
print("Program Finished!")