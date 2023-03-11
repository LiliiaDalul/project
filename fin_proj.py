#task 1

class Date:
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return "День: {}\tМесяц: {}\tГод: {}".format(self.day , self.month, self.year)

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        day, month, year = map(int, date.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 7777

    @staticmethod
    def from_string(date: str) -> 'Date':
        day, month, year = map(int, date.split('-'))
        new_date = day, month, year
        return new_date

date = Date.from_string('10-12-2077')
print(date)
print( Date.is_date_valid('10-12-2077'))
print( Date.is_date_valid('40-12-2077'))

#task 2

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")

a = int(input("Введите делимое:"))
b = int(input("Введите делитель:"))
div = DivisionByNull(a, b)
print(div.divide_by_null(a, b))

#task 3

class NotNumber(ValueError):
    pass

my_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'q':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as ex:
        print('Не число!', ex)
print(my_list)

#task 4,5,6

class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())

#task 7
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        return '{}{}{}i'.format(self.real, sign, self.imag)
    __repr__ = __str__

class ComplexCalc:
    def add(self, c1, c2):
        real = c1.real + c2.real
        imag = c1.imag + c2.imag
        return Complex(real, imag)
    def sub(self, c1, c2):
        real = c1.real - c2.real
        imag = c1.imag - c2.imag
        return Complex(real, imag)
    def mul(self, c1, c2):
        real = c1.real * c2.real - c1.imag * c2.imag
        imag = c1.imag * c2.real + c1.real * c2.imag
        return Complex(real, imag)
    def abs(self, c):
        return (c.real ** 2 + c.imag ** 2) ** 0.5

calc = ComplexCalc()
print(calc.add(Complex(1, 2), Complex(3, 4)))
print(calc.sub(Complex(1, 2), Complex(3, 4)))
print(calc.mul(Complex(1, 2), Complex(3, 4)))
print(calc.abs(Complex(3, 4)))