month = {1 : 'Зима', 2 : 'Зима', 3 : 'Весна', 4 : 'Весна', 5 : 'Весна', 6 : 'Лето', 7 : 'Лето', 8 : 'Лето', 9 : 'Осень', 10 : 'Осень', 11 : 'Осень', 12 : 'Зима'}
inp_month = int(input('Введите номер месяца: '))
while True:
    if inp_month >= 1 and inp_month <= 12:
        print(month.get(inp_month))
    break


