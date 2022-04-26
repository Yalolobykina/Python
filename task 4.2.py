my_tuple = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(my_tuple)
new_tuple = [el for el in my_tuple if my_tuple.count(el) == 1]
print(new_tuple)