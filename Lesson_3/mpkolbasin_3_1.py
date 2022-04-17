def division_1():
    el_1 = int(input("Введите число:"))
    el_2 = int(input("Введите число:"))
    try:
        return  el_1 / el_2
    except ZeroDivisionError:
        print("На 0 делить нельзя!")


print (division_1())