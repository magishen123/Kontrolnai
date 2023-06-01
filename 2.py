'''Класс «Автобус». Класс содержит свойства: – speed (скорость), –capacity (максимальное количество пассажиров), –
maxSpeed (максимальная скорость), – passengers (список имен пассажиров), – hasEmptySeats (наличие свободных мест), -
seats (словарь мест в автобусе); методы: – посадка и высадка одного или нескольких пассажиров, –
увеличение и уменьшение скорости на заданное значение. – операции "in", "+=" и "−=" (посадка и высадка пассажира(ов) с
заданной фамилией)'''

class Bus:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity
        self.currentPassengers = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self):
        self.speed = 0

    def getPassenger(self, count):
        if self.currentPassengers + count > self.capacity:
            raise ValueError("Мест нет")
        self.currentPassengers += count

    def dropPassenger(self, count):
        if self.currentPassengers - count < 0:
            raise ValueError("Автобус пуст, высаживать некого")
        self.currentPassengers -= count

    def __str__(self):
        return str([self.currentPassengers, self.speed])




Avtobus = Bus(100, 25)
Avtobus.accelerate(10)
Avtobus.getPassenger(10)
print(Avtobus)
Avtobus.dropPassenger(5)
print(Avtobus)