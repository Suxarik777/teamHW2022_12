

################################
######## обработка строк списка для user (доступ к функции только у админа)
def delete_row_user(array, index):
    print('Вы собираетесь удалить: \n', ' '.join(map(str, array[index])))
    user_in = int(input('''Вы действительно хотите удалить?: 
        0 - нет
        1 - да
        ввод: '''))
    if user_in == 0:
        return array
    elif user_in == 1:
        print('Запись удалена')
        del array[index]
        return array
    else:
        print('Некорректный ввод!')
        delete_row_user(index, array)
    return


def update_row_user(array, index):
    update_row = ' '.join(map(str, array[index]))
    print(f'Вы редактируете запись: \n{update_row}')
    print('''введите новые данные через пробел  ''') # небходимо уточнить что именно мы вводим
    sub_lst = input('→ ').split()

    sub_lst = forced_recording_serial_number_user(sub_lst, array[index][0])
    str_sub_lst = ' '.join(map(str, sub_lst))

    user_in = int(input(f'''Внести изменения? 
    Было: {update_row} 
    Стало: {str_sub_lst}
    0 - нет
    1 - да
    2 - повторить редактирование
    ввод: '''))

    if user_in == 0:
        return array
    elif user_in == 1:
        del array[index]
        array.insert(index, sub_lst)
        return array
    elif user_in == 2:
        return update_row_user(array, index)
    else:
        print('Некорректный ввод!, Начнем сначала :)')
        return update_row_user(array, index)


def add_row_user(array):
    how_to_print = ' '.join(map(str, array[0]))
    new_number_user = what_is_serial_number_new_user(array) #ищем новый-следующий номер для пользователя по списку
    print(f'''введите нового пользователя как в примере:  
    {how_to_print}
    порядковый номер нового пользователя: {new_number_user}''')
    sub_lst = input('→ ').split()

    sub_lst = forced_recording_serial_number_user(sub_lst, new_number_user) #принудительный чек порядкового номера
    str_sub_lst = ' '.join(map(str, sub_lst))

    user_in = int(input(f'''Внести нового пользователя? 
        {str_sub_lst}
        0 - нет
        1 - да
        2 - повторить
        ввод: '''))

    if user_in == 0:
        return array
    elif user_in == 1:
        array.append(sub_lst)
        return array
    elif user_in == 2:
        return add_row_user(array)
    else:
        print('Некорректный ввод!, Начнем сначала :)')
        return add_row_user(array)



# поиск нового порядкового номера пользователя
def what_is_serial_number_new_user(array):
    last_index_row = len(array) - 1
    last_number_user = int(array[last_index_row][0])
    next_number_user = last_number_user + 1
    return next_number_user

# Принудительная запись правильного порядкового номера пользователя
def forced_recording_serial_number_user(sub_lst, number):
    str_sub_lst = ' '.join(map(str, sub_lst))
    print(f'проверяем порядковый номер записи: \n{str_sub_lst} \nприсваиваем номер: {number}')
    if sub_lst[0].isdigit:
        sub_lst[0] = number
        return sub_lst
    else:
        sub_lst.insert(0, number)
        return sub_lst