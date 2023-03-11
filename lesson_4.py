#задание 1 - ничего не понятно, делаю все как описано, но не работает

import sys

hours, paym_hour, bonus = sys.argv

def salary_func(hours, paym_hour, bonus):
       try:
              print(f'Сотрудник заработал {int(hours) * int(paym_hour) * int(bonus)}')
       except TypeError:
              print('Конец расчета')
              exit()

salary_func(hours, paym_hour, bonus)

# задание 2
the_first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = []
for el in range(1, len(the_first_list)):
    if the_first_list[el] > the_first_list[el - 1]:
        result.append(the_first_list[el])

print(result)

# задание 2 вар 2
result = [the_first_list[el] for el in range(1,len(the_first_list)) if the_first_list[el] > the_first_list[el-1]]

print(result)

# задание 3
print([el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0])

# задание 4

the_first_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [el for el in the_first_list if the_first_list.count(el) == 1]

print(result)

# задание 5

from functools import reduce

new_list = [i for i in range(100,1001, 2)]

result = reduce((lambda x, y: x * y), new_list)

print(result)

#задание 6

from itertools import cycle, count

number_list = []

x = int(input('Введите первое число: '))
y = int(input('Введите последнее число: '))

#var 1
for i in count(x):
    if i > y:
        break
    print(i)
    number_list.append(i)

#var 2
number_list = [i for i in range(y)]
count = 0
for x in cycle(number_list):
    if count < y + 10:
        print(x)
        count += 1
    else:
        break

#задание 7

from itertools import count

def f(n):
    factorial = 1

    for x in count(1):
        if x > n:
            break

        factorial = factorial * x
        yield factorial

n = int(input("Введите целое неотрицательное число: "))
i = 0

for el in f(n):
    i += 1
    print(f'!{i} = {el}')