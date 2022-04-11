my_list = [7, 5, 3, 3, 2]
a = int(input("Введите число:"))
i = 0
for n in my_list:
    if a <= n:
        i += 1
my_list.insert(i, a)
print(my_list)