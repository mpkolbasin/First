# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open(r"file2.dat", 'w', encoding='utf-8') as f1:
    f1.write(f"{' '.join([str(i) for i in range(13, 24)])}")

with open(r"file2.dat", 'r', encoding='utf-8') as f1:
    numb_1 = [int(i) for i in f1.read().split()]
    print(sum(numb_1))
