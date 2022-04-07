inc = int(input('Введите сумму выручки: '))
exp = int(input('Введите сумму издержек: '))
profit = inc - exp
if profit > 0:
    print('Фирма работает с прибылью.')

    profit_r = profit / exp
    print('Рентабельность выручки: ' + (f'{profit_r}'))
    emp = int(input('Введите число сотрудников, чтобы вычислить прибыль в расчете на одного сотрудника: '))
    print(profit / emp)
else:
    print('Фирма работает с убытком.')