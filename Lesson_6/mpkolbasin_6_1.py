# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    __color = None

    def running(self, color="red"):
        while True:
            self.__color = "Red"
            print(f" TrafficLight is {self.__color} now")
            sleep(7)
            self.__color = "Yellow"
            print(f" TrafficLight is {self.__color} now")
            sleep(2)
            self.__color = "Green"
            print(f" TrafficLight is {self.__color} now")
            sleep(5)


traffic_1 = TrafficLight()
traffic_1.running()
