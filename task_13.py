# Задание №1
#
# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
#
# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

# class Cash:
#     money = 0
#
#     def __init__(self, m):
#         self.money = m
#
#     def top_up(self, insert):
#         self.money = insert + self.money
#
#     def count_1000(self):
#         if self.money:
#             c = self.money / 1000
#             return f"{int(c)} - целых тысяч осталось в кассе, {int(c * 1000)}₽."
#         else:
#             return 'дЭнЭг нЭт!'
#
#     def take_away(self, take):
#         if take <= self.money != 0:
#             self.money = self.money - take
#             return f'Забрали {take}₽. \nОсталось {self.money}₽.'
#         else:
#             return 'Денег нет, но вы держитесь! \nВам всего доброго, хорошего настроения и здоровья!'



# Задание №2
#
# Создайте класс Черепашка, который хранит позиции x и y черепашки,
# а также s - количество клеточек, на которое она перемещается за ход


# class Turtle:
#     def __init__(self, x, y, s):
#         self.x = x
#         self.y = y
#         self.s = s
#
#     def go_up(self):
#         self.y += self.s
#
#     def go_down(self):
#         self.y -= self.s
#
#     def go_left(self):
#         self.x -= self.s
#
#     def go_right(self):
#         self.x += self.s
#
#     def evolve(self):
#         self.s += 1
#
#     def degrade(self):
#         if self.s <= 1:
#             print("s не может быть ≤ 0")
#         else:
#             self.s -= 1
#
#     def count_moves(self, x2, y2):
#         dx = abs(x2 - self.x)
#         dy = abs(y2 - self.y)
#         moves_x = dx // self.s
#         if dx % self.s != 0:
#             moves_x += 1
#         moves_y = dy // self.s
#         if dy % self.s != 0:
#             moves_y += 1
#         return moves_x + moves_y
