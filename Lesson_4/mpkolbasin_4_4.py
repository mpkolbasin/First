# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите в порядке
# их следования в исходном списке. Для выполнения задания обязательно используйте генератор.

from random import randint

my_list_1 = []
for i in range(20):
    my_list_1.append(randint(0, 20))
print(my_list_1)
my_list_2 = {}
for j in my_list_1:
    if j in my_list_2:
        my_list_2[j] += 1
    else:
        my_list_2[j] = 1
result = [el for el in my_list_1 if my_list_2[el] == 1]
print(result)
