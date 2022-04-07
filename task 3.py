n = int(input('Ведите любое целое число: ')) # n - число для вывода в number_for_print
if n < 0:
    print('Введите число больше нуля!')
elif n > 0:
    print(int(n) + int(f'{n}{n}') + int(f'{n}{n}{n}'))
else:
    print('Введите число')