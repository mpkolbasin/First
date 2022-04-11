income_1 = int(input("Введите значение выручки:"))
expend_1 = int(input("Введите значение издержек:"))
if income_1 > expend_1:
    print("Результат работы фирмы - прибыль")
    rezult_1 = income_1 / expend_1
    print(f"Рентабельность выручки {rezult_1:.02f}")
    profit_1 = income_1 - expend_1
    print(f"Прибыль: {profit_1}")
    staff_1 = int(input("Введите количество сотрудников:"))
    profit_2 = profit_1 / staff_1
    print(f"Прибыль на одного сотрудника: {profit_2:.02f}")
else:
    print("Результат работы фирмы - убыток")