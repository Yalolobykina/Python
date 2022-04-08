name_1 = str(input('Введите название товара: '))
price_1 = int(input('Введите стоимость товара: '))
quantity_1 = int(input('Введите количество товара: '))
unit_1 = str(input('Введите единицу измередния количества товара: '))

name_2 = str(input('Введите название товара: '))
price_2 = int(input('Введите стоимость товара: '))
quantity_2 = int(input('Введите количество товара: '))
unit_2 = str(input('Введите единицу измередния количества товара: '))

name_3 = str(input('Введите название товара: '))
price_3 = int(input('Введите стоимость товара: '))
quantity_3 = int(input('Введите количество товара: '))
unit_3 = str(input('Введите единицу измередния количества товара: '))

name_4 = str(input('Введите название товара: '))
price_4 = int(input('Введите стоимость товара: '))
quantity_4 = int(input('Введите количество товара: '))
unit_4 = str(input('Введите единицу измередния количества товара: '))

items_1 = [1, {'Название товара': name_1, 'Цена' : price_1, 'Количество' : quantity_1, 'Ед.' : unit_1}]
items_2 = [2, {'Название товара': name_2, 'Цена' : price_2, 'Количество' : quantity_2, 'Ед.' : unit_2}]
items_3 = [3, {'Название товара': name_3, 'Цена' : price_3, 'Количество' : quantity_3, 'Ед.' : unit_3}]
items_4 = [4, {'Название товара': name_4, 'Цена' : price_4, 'Количество' : quantity_4, 'Ед.' : unit_4}]

print(items_1)
print(items_2)
print(items_3)
print(items_4)

items_dict_1 = items_1[1]
items_dict_2 = items_2[1]
items_dict_3 = items_3[1]
items_dict_4 = items_4[1]


names = [items_dict_1 ['Название товара'], items_dict_2 ['Название товара'], items_dict_3 ['Название товара'], \
         items_dict_4 ['Название товара']]
names_dict = {'Название товара' : names}

prices = [items_dict_1['Цена'], items_dict_2['Цена'], items_dict_3['Цена'], items_dict_4['Цена']]
prices_dict = {'Цена' : names}

quantities = [items_dict_1['Количество'], items_dict_2['Количество'], items_dict_3['Количество'], items_dict_4['Количество']]
quantities_dict = {'Количество' : names}

units = [items_dict_1['Ед.'], items_dict_2['Ед.'], items_dict_3['Ед.'], items_dict_4['Ед.']]
units_dict = {'Ед.' : names}

print(names_dict)
print(prices_dict)
print(quantities_dict)
print(units_dict)

