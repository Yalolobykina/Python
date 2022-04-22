def division():
    a = int(input('Введите числитель: '))
    b = int(input('Введите знаменатель: '))
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
division()