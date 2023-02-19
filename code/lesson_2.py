#задание 1
var_list = [19, -19, True, 'Pavel', 1.5, None]
for el in var_list:
    print(type(el))

#задание 2
var_list = input("Укажите целые числа через пробел:").split(' ')
i, j = 0, 1
while len(var_list) > j:
    var_list[i], var_list[j] = var_list[j], var_list[i]
    i += 2
    j += 2
print(*var_list)

#задание 3.1
month_list = [None, "Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень",
              "Осень", "Зима"]
month_number = int(input('Введите номер месяца от 1 до 12:'))
print(f'Время года: {month_list[month_number]}')

#задание 3.2
month_list = {1:"Зима", 2:"Зима", 3:"Весна", 4:"Весна", 5:"Весна",
              6:"Лето", 7:"Лето", 8:"Лето", 9:"Осень", 10:"Осень", 11:"Осень", 12:"Зима"}
month_number = int(input('Введите номер месяца от 1 до 12:'))
print(f'Время года: {month_list.get(month_number)}')

#задание 4
user_script = input('Введите несколько слов, разделенных пробелами:').split(' ')
for ind, el in enumerate(user_script):
    print(ind, el[0:10])

#задание 5
current_list = [5, 4, 3, 2]
while True:
    user_num = input('Введите число от 1 до 9 или "Конец" для выхода:')
    if user_num != "Конец":
        current_list.append(int(user_num))
        current_list.sort(reverse=True)
        print(current_list)
    else:
        break
 #the end