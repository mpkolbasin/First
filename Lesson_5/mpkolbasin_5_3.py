# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад
# менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней
# величины дохода сотрудников.

with open(r"text_3.txt", 'r', encoding='utf-8') as f1:
    names = []
    aver_1 = 0
    num = 0
    for line in f1:
        num += 1
        name, income = (i for i in line.split())
        income = float(income)
        if income < 20000:
            names.append(name)
        aver_1 += income
    aver_1 /= num
print("Сотрудника с окладом меньше 20К: ", *names)
print(f"Средний доход: {aver_1:.02f}")
