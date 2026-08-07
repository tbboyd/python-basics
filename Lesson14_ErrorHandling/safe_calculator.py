while True:

    try:
        number1 = int(input('Enter your first number: '))
        number2 = int(input('Enter your second number: '))

        answer1 = number1 + number2
        answer2 = number1 - number2
        answer3 = number1 * number2
        answer4 = number1 / number2

        print(answer1)
        print(answer2)
        print(answer3)
        print(answer4)

        break

    except ValueError:
        print('Please enter a valid number.')

    except ZeroDivisionError:
        print('You cannot divide by zero.')
