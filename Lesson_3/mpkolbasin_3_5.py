def my_func():
    count_1 = 0
    list_1 = input("Ввведите последовательность чисел через пробел и Q для выхода :").upper().split()
    for i in list_1:
        if i == "Q":
            return count_1, True
        try:
            count_1 += int(i)
        except ValueError:
            pass
    return count_1, False


result_1 = 0
while True:
    a, b = my_func()
    result_1 += a
    print(result_1)
    if b:
        break