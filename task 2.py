seconds = int(input('Введите время в секундах: '))
minutes = seconds / 60
hours = int(minutes / 60)
min_print = int(minutes % 60)
sec_print = int(seconds % 60 % 60)
print(f'Вы ввели время: {hours} час(ов) : {min_print} минут(а) : {sec_print} секунд(а)')