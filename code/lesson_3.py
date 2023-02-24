#задание 1
def division_func(* args):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Zero value division'

try:
    user_numbers = input('Введите делимое и делитель через запятую:').split(',')
    a = int(user_numbers[0])
    b = int(user_numbers[1])
    print(division_func(a,b))
except ValueError:
    print('Only numbers are allowed')


#задание 2
name = input('Введите свое имя:')
surname = input('Введите свою фамилию:')
b_day = input('Введите свой день рождения:')
city = input('Укажите город проживания:')
email = input('Укажите свой email:')
phone = input('Укажите свой номер телефона:')

def user_info(** kwargs):
    print(f'ФИО: {name} {surname}, день рождения: {b_day}, город проживания: {city}, почта: {email}, телефон: {phone}')

user_info(
name = name,
surname = surname,
b_day = b_day,
city = city,
email = email,
phone = phone
)

#задание 3 вариант 1
num_1 = int(input('Введите первое число:'))
num_2 = int(input('Введите второе число:'))
num_3 = int(input('Введите третье число:'))
def my_funct(num_1, num_2, num_3):
    user_number = [num_1, num_2, num_3]
    user_number.pop(user_number.index(min(user_number)))
    res = sum(user_number)
    return res
res = my_funct(num_1, num_2, num_3)
print(res)

#задание 3 вариант 2
def my_funct7(* args):
    print(sum(sorted(list(args), reverse=True)[:2]))

my_funct7(1,4,20)


#задание 3 вариант 3
def my_funct2(* args):
    arg_list = list(args)
    i = 0
    result = 0
    while i != 2:
        max_number = max(arg_list)
        result += max_number
        arg_list.remove(max_number)
        i += 1
    print(result)

my_funct2(10,2,12)


#Задание 4
x = int(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
def xy_pow(x,y):
    xypow = 1 / x ** abs(y)
    return xypow
xypow = xy_pow(x,y)
print(xypow)

a = pow(2,-1)
print(a)

#задание 4 вариант 2
x = int(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
def square_xy(x,y):
    try:
        if y < 0:
            result = 1
            for i in range(y,0):
                result = result * x
            result = 1 / result
            return result
        else:
            return "Число должно быть отрицательным"
    except TypeError:
        return "Только числовые значения"
    except ZeroDivisionError:
        return "Деление на 0"

print(square_xy(x,y))

#Задание 5

def num_counter(current_sum=0):
    user_num = input('Введите любое количество чисел, разделенных пробелом или "Конец": ').split(' ')
    for el in range(len(user_num)):
        if user_num[el] != "Конец":
            current_sum = current_sum + int(user_num[el])
        else:
            break
    print(current_sum)
    if "Конец" in user_num:
        exit('Выполнение программы завершено')
    else:
        num_counter(current_sum)

num_counter()

#Задание 6
def int_func(string):
    return string.title()
print(int_func('text'))

#Задание 7
def title_func(string):
    title_list = []
    fst = string.split()
    for el in fst:
        title_list.append(int_func(el))
    print(*title_list)

title_func('первое слово дороже второго')



