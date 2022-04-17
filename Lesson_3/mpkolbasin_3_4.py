def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print("Вводите только действительное первое число и целое второе число ")
        return
    if x <= 0 or y >= 0:
        print("Вводите только положительное первое число и отрицательное второе число ")
        return
    return x ** y


print(round(my_func(input("Введите первое число: "), input("Введите второе число: ")), 10))