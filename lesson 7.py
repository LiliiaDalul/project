#задание 1
from typing import List

class Matrix:
    def __init__(self, *args):
        self.new_list = list(args)

    def __str__(self):
        result = '\n'.join(map(str, self.new_list))
        result = result.replace(',', '').replace('[', '').replace(']', '')
        return result

    def __add__(self, other):
        new_sum = []
        line_sum = []
        for x in range(len(self.new_list)):
            for y in range(len(self.new_list[x])):
                line_sum.append(self.new_list[x][y] + other.new_list[x][y])
            new_sum.append(line_sum)
            line_sum = []
        return Matrix('\n'.join(map(str, new_sum)))

M_OBJ_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(M_OBJ_1)
print()

M_OBJ_2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(M_OBJ_2)
print()

print(f'Сумма матриц: \n{M_OBJ_1 + M_OBJ_2}')

#задание 2

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expense(self):
        pass

    def __str__(self):
        return str(self.param)


class Coat(Clothes):

    @property
    def expense(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def expense(self):
        return self.param * 2 + 0.3


a = Coat(52)
b = Suit(1.80)
print(a)
print(a.expense)
print(b.expense)


#задание 3


class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.simbol = '*'

    def __str__(self):
        return str(f'Количество ячеек - {self.cell}')

    def __sub__(self, other):
        return Cell(abs(self.cell - other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __add__(self, other):
        return Cell(abs(self.cell + other.cell))

    def make_order(self, count):
        x = self.cell
        while x > 0:
            for k in range(1, count + 1):
                print(self.simbol, end='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end='')


a = Cell(5)
b = Cell(10)
c = Cell(3)
d = Cell(2)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

a.make_order(3)
b.make_order(3)
