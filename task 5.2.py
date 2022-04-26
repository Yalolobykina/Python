from functools import reduce

my_list = list(range(100,1001))
def new_func(i, el):
    return i * el

print(f'{my_list}\n', reduce(new_func, my_list))