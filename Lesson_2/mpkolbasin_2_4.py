my_list = input("Введите предложение используя пробелы:").split()
for i, word_1 in enumerate (my_list, 1):
    print(f"{i} {word_1[:10]}")