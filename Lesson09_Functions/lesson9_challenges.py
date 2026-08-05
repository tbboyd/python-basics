## ==== Challenge 1 ====

def say_hello():
    print('Hello!')

count = 1

while count <= 5:
    say_hello()
    count += 1

## ==== Challenge 2 ====

def favorite_game(game):
    print('My favorite games is', game)

favorite_game('league of legends')
favorite_game('roblox')
favorite_game('rocket league')

## ==== Challenge 3 ====

def multiply(a, b):
    return a * b

answer = multiply(2, 5)

print(answer)

## ==== Challenge 4 ====

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    return balance - amount

def show_balance(balance):
    return balance

deposit1 = deposit(500, 250)
withdraw1 = withdraw(deposit1, 100)
print(show_balance(withdraw1))