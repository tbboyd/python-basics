animals = ["Dog", "Cat", "Bird"]

print(animals)

animals.append("Fish")

print(animals)

animals = ["Dog", "Cat", "Bird"]

animals.insert(1, "Fish")

print(animals)

animals = ["Dog","Cat","Bird","Fish"]

animals.remove("Bird")

print(animals)

numbers = [10,20,30,40]

numbers.pop(2)

print(numbers)

numbers = [12, 7, 35, 20, 18]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print('Largest:', largest)