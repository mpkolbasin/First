def my_func(el1, el2, el3):
    try:
        return sum((el1, el2, el3)) - min(el1, el2, el3)
    except:
        return "Вводите только числа"


print(my_func(6, 8, 4))