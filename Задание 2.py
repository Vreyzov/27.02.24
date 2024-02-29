def ask_password():
    password = "password"
    attempts = 3

    while attempts > 0:
        user_input = input("Введите пароль: ")

        if user_input == password:
            print("Пароль принят")
            break
        else:
            attempts -= 1

    if attempts == 0:
        print("В доступе отказано")