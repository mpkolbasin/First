n = int(input ("Введите целое положительное число:"))
b = 1
itog_1 = 0
while b != 0:
    a = n % 10
    b = n // 10
    n = b
    if a > itog_1:
        itog_1 = a


print(f"Самая большая цифра в числе: {itog_1}")