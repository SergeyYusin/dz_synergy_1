# Задание №1
#
# Создайте объект Autobus, который унаследует все переменные и
# методы родительского класса Transport и выведете его.
# Ожидаемый результат вывода:
#
# Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

# class Transport:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def autobus(self):
#         return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"
#
#
# Autobus = Transport('Renaul Logan', 180, 12)
#
# print(Autobus.autobus())


# Задание №2
#
# Создайте класс Autobus, который наследуется от класса Transport.
#
# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
#
# Используйте переопределение метода.
#
# Используйте следующий код для родительского класса транспортного средства:


# class Transport:
#
#    def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#    def seating_capacity(self, capacity):
#       return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"
#
#
# class Autobus(Transport):
#     def seating_capacity(self, capacity=50):
#        return super().seating_capacity(capacity)
#
#
# autobus = Autobus('Renaul Logan', 180, 12)
# print(autobus.seating_capacity())