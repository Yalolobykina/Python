def info():
    name = str(input('Укажите ваше имя: '))
    surname = str(input('Укажите вашу фамилию: '))
    birth = str(input('Укажите дату рождения в формате дд.мм.гггг.: '))
    place = str(input('Укажите ваш город: '))
    mail = str(input('Укажите ваш email: '))
    t_num = str(input('Введите номер телефона: '))
    info_dict = {'Имя' : name, 'Фамилия' : surname, 'Дата рождения' : birth, 'Город проживания' : place, 'email' : mail, 'Номер телефона' : t_num}
    return info_dict

info_p = info()
print('Информация о Вас: ' + (str(info_p)))




