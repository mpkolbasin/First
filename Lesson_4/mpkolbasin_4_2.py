# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

from random import randint

my_list_1 = []
for i in range(20):
    my_list_1.append(randint(0, 300))

print(my_list_1)
print([a for b, a in enumerate(my_list_1) if b != 0 and a > my_list_1[b - 1]])
