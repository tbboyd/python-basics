grades = { 

    'Alice': 95,
    'Trystan': 80, 
    'Bob': 85,

}

print(grades['Alice'])

grades['Bob'] = 80
grades['Charlie'] = 90

print(grades['Bob'])
print(grades)

del grades['Bob']
print(grades)

print(len(grades))
print('Bob' in grades)
print('Alice' in grades)