password = "python123"

while True:

    attempt = input("Enter password: ")

    if attempt == password:

        print("Access Granted!")

        break

    else:

        print("Incorrect Password.")