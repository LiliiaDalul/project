#задание 1

new_file = open("new_fyle.txt", 'a')
while True:
    s = input("Введите текст, чтобы выйти из режима редактирования введите пустую сторку: ")
    if s == '':
        break
    new_file.write(s+'\n')
new_file.close()

#задание 2
lines_counter = 0
words_counter = 1
with open(r"C:\Users\79959\Desktop\for_python_pro.txt", 'r') as source_doc:
    for line in source_doc:
        print(line.replace('\n', ''))
        for n in line:
            if n == " ":
                words_counter += 1
        lines_counter += 1
        print(f"Кол-во слов в строке {lines_counter}  = {words_counter}")
        words_counter = 1
    print(f"В файле {lines_counter} строк")

#задание 3
i = 0
sum_sal = 0
with open(r'C:\Users\79959\Desktop\salary_list.txt', 'r') as source_doc:
    workers = {}
    for line in source_doc:
        key, value = line.split()
        workers[key] = value
        i += 1
        sum_sal += int(value)
        if float(value) < 20000:
            print(f'{key}: зарплата меньше 20000')
average_sal = int(sum_sal / i)
print(f"Средняя зарплата = {average_sal}")

# задание 4
dict_trans = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open(r"C:\Users\79959\Desktop\числа.txt", 'r') as dict_source:
    for line in dict_source:
        for key in dict_trans.keys():
            line = line.replace(key, dict_trans[key])
        print(line)
        with open(r"copy_file.txt", 'a') as dict_rus:
            dict_rus.write(f"\n {line}")

# Задание 5
def summary():
    while True:
        try:
            with open(r"C:\Users\79959\Desktop\числа 3.txt", 'w+') as file_obj:
                line = input('Введите цифры через пробел \n')
                file_obj.writelines(line)
                my_numb = line.split()
                print(sum(map(int, my_numb)))
            if line == '':
                break
        except IOError:
            print('Ошибка в файле')
        except ValueError:
            print('Неправильно набран номер. Ошибка ввода-вывода')
summary()

# задание 6

import json
subj = {}
with open(r"C:\Users\79959\Desktop\предметы.txt", 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')

# задание 7
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')


