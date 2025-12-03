def password_generator():
    import random
    print("Создадим пароль под ваши параметры")
    while True:
        try:
            length = int(input("Введите длину пароля: "))
            print("В случае ответа 'нет' - любое другое значение")
            spec_symbols_value = input("Использовать специальные символы? (да или нет): ")
            words_lower_value = input("Использовать строчные буквы? (да или нет): ")
            words_upper_value = input("Использовать заглавные буквы? (да или нет): ")
            numbers_value = input("Использовать числа? ")


            def generate_password():
                symbols = "!#$%&'\"()*+,-./:;<=>?@[\]^_`{|}~"
                words_lower = "abcdefghijklmnopqrstuvwxyz"
                words_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                numbers = "0123456789"
                all_elements = words_lower + words_upper + numbers + symbols
                approved_list = []

                if spec_symbols_value in 'ДадаДА':
                    approved_list.append(symbols)

                if words_lower_value in 'ДадаДА':
                    approved_list.append(words_lower)

                if words_upper_value in 'ДадаДА':
                    approved_list.append(words_upper)

                if numbers_value in 'ДадаДА':
                    approved_list.append(numbers)

                approved_list = "".join(approved_list)
                generated_password = ("".join(random.sample(approved_list, length)))
                print("Сгенерированный пароль: ", generated_password)
                return generated_password

            password = generate_password()

            def safe_status():
                if len(password) < 10:
                    print("Длина вашего пароля мала для хорошей надежности\nРекомендуемая длина составляет минимум 10 символов")
                if len(password) > 128:
                    print("Ваш пароль слишком длинный, поэтому он не является рабочим")
                if 10 <= len(password) <= 128:
                    print("Длина вашего пароля является надежной")

                check_numbers = any(c.isdigit() for c in password)
                if check_numbers is True:
                    print("В вашем пароле присутствуют числа, что делает его надежнее")
                if check_numbers is False:
                    print("В вашем пароле отсутствуют числа, что делает его ненадежнее")

                check_words = any(c.isalpha() for c in password)
                if check_words is True:
                    print("В вашем пароле присутствуют буквы, что делает его надежнее")
                if check_words is False:
                    print("В вашем пароле отсутствуют буквы, что делает его ненадежнее")

                check_symbols = any(not c.isalnum() for c in password)
                if check_symbols is True:
                    print("В вашем пароле присутствуют специальные символы, что делает его надежнее")
                if check_symbols is False:
                    print("В вашем пароле отсутствуют специальные символы, что делает его ненадежнее")
            safe_status()

        except Exception:
            print("В программе произошла ошибка, попробуйсте снова")
    