while True:

    try:

        age = int(input("Enter your age: "))

        break

    except ValueError:

        print("Please enter numbers only.")

print()

print("Age:", age)