def OddEven(n):
    if n%2 == 0:
        return 'Even'
    else:
        return 'Odd'


OddEven = lambda n:(n%2 and 'OOD' or 'EVEN')

print(OddEven(14))
print(OddEven(15))

