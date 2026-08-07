import random

charaters = (

    'ABCDEFGHIJKLOMNPQRSTUVWXYZ'
    'abcdefghijklomnpqrstuvwxyz'
    '0123456789'
    '!@#$%^&*'

)

password = ''

for i in range(12):
    password += random.choice(charaters)

print("==== Password Generator ====")
print()
print("Generated Password:")
print(password)