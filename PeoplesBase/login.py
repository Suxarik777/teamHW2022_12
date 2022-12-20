def login():# При успешной регистрации возвращает user_id и user_type. При не успешной возвращает (-1).
    with open('users.csv', 'r', encoding='utf-8') as f:
        users = f.readlines()

    print("Для входа в приложение, введите свой login и password")
    
    for i in range(1, 4):
        user_login = input("Введите login: ")
        user_pass = input("Введите password: ")

        for item in users:
            res = item.split(';')

            if res[3] == user_login and res[4] == user_pass:
                print("Вход выполнен успешно")
                print(f"Рады Вас видеть {res[1]}!!!")
                return res[0], res[5]

        print("Вы ввели не верные данныеб осталось попыток: ", (3 - i))

    print("Вы три раза ввели не верные данные! Обратитесь в службу поддержки!")
    return -1
