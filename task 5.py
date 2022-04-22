def summa():
    n = 0
    guest_list = input('Введите числа, которые Вы хотите сложить. Для выхода из программы введите X: ').upper().split()
    for i in guest_list:
        if i == 'X':
            return n, True
        try:
            n += int(i)
        except ValueError:
            pass
    return n, False

z = 0
while True:
    a, b = summa()
    z += a
    print(z)
    if b:
        break




