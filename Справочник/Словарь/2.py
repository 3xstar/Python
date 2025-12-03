assets = {"anecdots": ["Максим Сюзюмов пришел на пару","В РПО2 адекватные люди"],
          "predictions": ["Максим Сюзюмов не придет на пару","В РПО 2 все сдали модули на 5"]}

import random

while True:
    print("1. Дать андекдот"
          "\n2. Дать предсказание,"
          "\n3. Добавить Анекдот,"
          "\n4. Добавить предсказание")
    action = int(input("Ваши действия: "))

    match action:
        case 1:
            random_anecdot = random.choice(assets["anecdots"])
            print(random_anecdot)
        case 2:
            random_prediction = random.choice(assets["predictions"])
            print(random_prediction)
        case 3:
            new_anecdot = input("Введите новый анекдот: ")
            assets["anecdots"].append(new_anecdot)
            print(f"Анекдот: {new_anecdot} добавлен")
        case 4:
            new_prediction = input("Введите новое предсказание: ")
            assets["predictions"].append(new_prediction)
            print(f"Предсказание: {new_prediction} добавлено")