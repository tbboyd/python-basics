age = int(input('How old are you? '))

print()
print('==== Age ====')
print('Adult: ', age >= 19)
print('Can retire: ', age >= 65)
print('Teen: ', age >= 13 and age <= 19)

