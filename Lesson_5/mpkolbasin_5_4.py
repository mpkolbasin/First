# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict_1 = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open(r"text_4.txt", 'r', encoding='utf-8') as f1:
    with open(r"text_5.txt", 'w', encoding='utf-8') as f2:
        for line in f1:
            en, *num = line.split()
            ru = dict_1[en]
            f2.write("".join([ru] + num) + "\n")
