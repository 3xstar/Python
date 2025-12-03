import random


def numbers_password():
    i = 0
    while True:
        i += 1
        yield i


def latter_password(length):
    latters = ["a", "b", "c", "d", "e", "1", "2", "3"]
    while True:
        password = ""
        for i in range(length):
            password += random.choice(latters)
        yield password


def main():
    password = input("Введите пароль: ")

    type = input("Пароль состоит из 1.букв или 2.цифр?: ")

    if type == "1":
        length = int(input("Введите длину пароля: "))
        generator = latter_password(length)
        gen_password = next(generator)
        while password != gen_password:
            gen_password = next(generator)

    elif type == "2":
        password = int(password)
        generator = numbers_password()
        gen_password = next(generator)
        while password != gen_password:
            gen_password = next(generator)

    print(gen_password)

if __name__ == "__main__":
    main()
