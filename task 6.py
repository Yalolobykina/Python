from itertools import cycle

my_list = [2, 'cats', 'see', 5, 'dogs']

i = 0
for el in cycle(my_list):
    if i >= 10:
        break
    print(el)
    i += 1

