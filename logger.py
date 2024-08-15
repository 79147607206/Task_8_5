from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n")

 
def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = 1
        print(''.join(data_first_list))


    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def copy_data():
    data_to_copy = ""
    f_num = int(input("Введите номер файла откуда надо скопировать строку [1, 2]: "))
    while f_num > 2 and f_num < 1:
        f_num = int(input("Введите номер файла откуда надо скопировать строку [1, 2]: "))

    if f_num == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()
            s_num = int(input(f"В первом файле {len(data)} строк!\nВведите строку, которую хотите скопировать с первого файла во второй: "))

            while s_num > len(data):
                print(f"Вы ввели несуществующий номер строки!Введите число от 1 до {len(data)}!")
                s_num = int(input(f"Введите строку, которую хотите скопировать с первого файла во второй: "))

            data_to_copy = data[s_num - 1]

        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(data_to_copy)
        print(f"Строка {s_num} была успешно скопирована в конец второго файла!")

    elif f_num == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()

            s_num = int(input(
                f"Во втором файле {len(data)} строк!\nВведите строку, которую хотите скопировать со второго файла в первый: "))

            while s_num > len(data):
                print(f"Вы ввели несуществующий номер строки!Введите число от 1 до {len(data)}!")
                s_num = int(input(f"Введите строку, которую хотите скопировать со второго файла в первый: "))

            data_to_copy = data[s_num - 1]

        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(data_to_copy)
        print(f"Строка {s_num} была успешно скопирована в конец первого файла!")



