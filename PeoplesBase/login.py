def login():# При успешной регистрации возвращает user_id и user_type. При не успешной возвращает (-1).
    with open('user.csv', 'r', encoding='utf-8') as f:
        users = f.readlines()

    print("To enter input login and password")
    
    for i in range(1, 4):
        user_login = input("Input login: ")
        user_pass = input("Input password: ")

        for item in users:
            res = item.split(';')

            if res[3] == user_login and res[4] == user_pass:
                print("Login succesfull")
                print(f"Wellcome {res[1]}!!!")
                return res[0], res[5]

        print("Not right data tres left: ", (3 - i))

    print("Wrong data contact support")
    return -1
