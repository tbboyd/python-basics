import random

name = input('What is your name? ')

lucku_games = [

    'League of legends',
    'Valorant',
    'Roblox',
    'Rocket league',
    'Call of duty'

]

print('Hello', name + '!')
print()
print('Your lucky game today is '+ random.choice(lucku_games) + '!')