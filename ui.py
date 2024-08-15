from logger import input_data, print_data, copy_data

def interface():
    print("Добрый день! Вы попали на специальной бот справочник от GeekBrains! \n 1 -запись данных \n 2- вывод данных \n "
          "3 - копирование данных")
    command = int(input('Ведите число '))

    while command != 1 and command != 2 and command != 3:
        print("Неправельный ввод")
        command = int(input('Введите число '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        copy_data()