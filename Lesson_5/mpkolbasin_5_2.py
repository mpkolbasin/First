# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

num_words = 0

with open(r"file1.dat", 'r', encoding='utf-8') as f1:
    str_1 = sum(1 for line in f1)
    with open(r"file1.dat", 'r', encoding='utf-8') as f1:
        for line_1 in f1:
            words = line_1.split()
            num_words += len(words)
    print("Число строк: ", str_1)
    print("Число слов: ", num_words)
