client_str = str(input('Введите любое предложение, состоящее из нескольких слов: '))
client_str = client_str.split()
line = 0
for el in client_str:
    line += 1
    print(line, el[:10])


