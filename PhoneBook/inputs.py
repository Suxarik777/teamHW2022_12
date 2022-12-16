import csv
from outputs import print_menu


def input_row(array):
    choosen_source = input('Для выбора способа ввода данных, введите: '
                           '\n\t0 - ввод с клавиатуры '
                           '\n\t1 - ввод из файла\n')
    if choosen_source == '0':
        return input_console(array)
    elif choosen_source == '1':
        source_path = input('Напишите путь к файлу для записи\n')
        return input_file(source_path, array)


def input_console(array):
    manual_data = input('Введите данные в формате \n"Имя;Фамилия;Телефон;Комментарий"\n')
    data_list = manual_data.split(';')
    print(data_list)
    array.append(data_list)
#    return data_list


def input_file(source_path, data_list_file):
    with open(source_path, 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=';', skipinitialspace=False)
#        data_list_file = []
        for line, row in enumerate(file_reader):
            if line>1:
                file_reader_to_list = (';'.join(row)).split(';')
                data_list_file.append(file_reader_to_list[1:])
#        return data_list_file


def input_index(arr) -> int:
#    input_file()
    uncorrect = True
    while uncorrect:
        row_numb = int(input('Введите номер требуемой записи'))
        if row_numb <= len(arr):
            uncorrect = False
            return row_numb
        else: print('Warning! Inputed Index Is Out Of Range\nTry Again')
        uncorrect = True



def input_string() -> str:
    inputed_string = input('Введите строку в формате\nИмя;Фамилия;Телефон;Комментарий')
    return inputed_string


def input_menu_item() -> int:
    MENU_ITEMS = 7
    uncorrect = True
#    menu_item = int(input('Введите пункт меню\n'))
    while uncorrect:
        menu_item = int(input('Введите пункт меню\n'))
        if menu_item <= MENU_ITEMS:
            uncurrect = False
            return menu_item
        else:
            print("Введите пункт меню заново\n")
            uncurrect = True

