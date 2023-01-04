


# функция удаления записи в базах
def delete_row(array, index):
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
        delete_row(index, array)


# функция редактирование записи в базах
def update_row(array, index):
    str_update_row = ' '.join(map(str, array[index]))
    print(f'Вы редактируете запись: \n{str_update_row}')
    print('введите новые данные через пробел  ')
    # небходимо уточнить что именно мы вводим
    sub_lst = input('→ ').split()

    sub_lst = forced_recording_id_database(sub_lst, array[index][0])
    str_sub_lst = ' '.join(map(str, sub_lst))

    user_in = int(input(f'''Внести изменения? 
    Было: {str_update_row} 
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
        return update_row(array, index)
    else:
        print('Некорректный ввод!, Начнем сначала :)')
        return update_row(array, index)


# добавление записи в базу
def add_row(array):
    how_to_print = ' '.join(map(str, array[0]))
    new_number_user = what_is_id_new_database_entry(array)  # ищем след id для записи
    print(f'''введите новую запись как в примере:  
    {how_to_print}
    id новой записи: {new_number_user}''')
    sub_lst = input('→ ').split()

    sub_lst = forced_recording_id_database(sub_lst, new_number_user)  # принудительный чек id
    str_sub_lst = ' '.join(map(str, sub_lst))

    user_in = int(input(f'''Внести новую запись? 
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




########## вспомогательные функции для работы основных функций выше
# поиск нового id номера в базе для новой записи
def what_is_id_new_database_entry(array):
    last_index_row = len(array) - 1
    last_number_user = int(array[last_index_row][0])
    next_number_user = last_number_user + 1
    return next_number_user


# Принудительная запись правильного id номера записи
def forced_recording_id_database(sub_lst, number):
    str_sub_lst = ' '.join(map(str, sub_lst))
    print(f'проверяем порядковый номер записи: \n{str_sub_lst} \nприсваиваем номер: {number}')
    if sub_lst[0].isdigit:
        sub_lst[0] = number
        return sub_lst
    else:
        sub_lst.insert(0, number)
        return sub_lst

