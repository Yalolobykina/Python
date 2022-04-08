list_1 = []
len_list_1 = 7
inp_list_1 = 1
while inp_list_1 <= len_list_1:
    client_list = input(f'Введите {inp_list_1}-й элемент списка: ')
    list_1.append(client_list)
    inp_list_1 += 1
print(list_1)
list_1[0], list_1[1] = list_1[1], list_1[0]
list_1[2], list_1[3] = list_1[3], list_1[2]
list_1[4], list_1[5] = list_1[5], list_1[4]
print(list_1)
