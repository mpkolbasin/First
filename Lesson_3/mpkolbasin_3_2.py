def users_inf_1(**kwargs):
    return " ".join(kwargs.values())

print(users_inf_1(name_1=input("Введите Ваше Имя: "), surname_1=input("Введите Вашу Фамилию: "),
                  birth_year_1=input("Введите Ваш год рождения: "), city_1=input("Введите Ваш город: "),
                  email_1=input("Введите Ваш эл. адрес: "), phone_1=input("Введите Ваш телефон: ")))