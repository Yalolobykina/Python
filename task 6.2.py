from itertools import count

for el in count(1, 2):
    if el > 10:
        break
    print(el)

