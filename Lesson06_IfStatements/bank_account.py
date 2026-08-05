bank_balance = float(input('What is your account balance? '))
withdraw = float(input('How much would you like to withdraw? '))

if withdraw <= bank_balance:
    print('Withdrawal Approved.')
else: 
    print('Insuffecient Funds.')

print('Transaction Complete')

age = int(input('How old are you? '))

if age >= 13:
    print('Welcome in and enjoy the movie.')
else:
    print('Sorry you are too young.')

print('Age check complete.')