hourly_rate = float(input('What is your hourly rate? '))
weekly_hours_worked = int(input('How many hours have you worked this week? '))
tax_percentage = int(input('What perecentage of your income is taxed? '))

gross_pay = hourly_rate * weekly_hours_worked
taxes = gross_pay * (tax_percentage / 100)
net_pay = gross_pay - taxes

print()
print('==== Weekly Paycheck ====')
print('Hourly rate: $', hourly_rate)
print('Hours worked: ', weekly_hours_worked)
print('Gross Pay: $', gross_pay)
print('Taxes: $', taxes)
print('Net Pay: $', net_pay)