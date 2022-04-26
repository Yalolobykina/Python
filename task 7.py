def factorial(i):
    for el in range(1, i+1):
        yield el

my_factorial = 1
for el in factorial(15):
    my_factorial *= el

print(my_factorial)