def int_func(word):
    latin_char = "abcdifghijklmnopqrstuvwxyz"
    return word.title() if not set(word).difference(latin_char) else False


words = input("Введите строку на латинице строчными буквами: ").split()
for i in words:
    result = int_func(i)
    if result:
        print(int_func(i), " ")