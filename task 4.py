my_tuple = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

repeat = set()
unique = set()

for el in my_tuple:
    if el in repeat:
        continue
    if el in unique:
        repeat.add(el)
        unique.discard(el)
        continue
    unique.add(el)
print(unique)

new_tuple = [el for el in my_tuple if el in unique]
print(new_tuple)