def int_func(word):
    letter = word[0]
    assert letter >= 'a' and letter <= 'z' and word[0].islower()
    return word.title()

print(int_func('wordstr'))
print(int_func('word str in line'))
