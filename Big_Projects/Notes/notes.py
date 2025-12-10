import json
import datetime

def get_formatted_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def add_note(title, text):
    try:
        with open('notes.json', 'r', encoding='UTF-8') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

    if notes:
        max_id = max(note["id"] for note in notes)
        next_id = max_id + 1
    else:
        next_id = 1

    data = {
        "id": next_id,
        "title": title,
        "text": text
    }

    notes.append(data)

    with open('notes.json', 'w', encoding='UTF-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

    print(f"Заметка добавлена под данным id: {next_id}\n")

    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(f"{get_formatted_time()} - добавлена заметка под id: {next_id}\n")


def get_note(id):
    try:
        with open('notes.json', 'r', encoding='UTF-8') as file:
            notes = json.load(file)
    except FileNotFoundError:
        print("Нечего находить когда заметок нет\n")
        with open('log.txt', 'a', encoding='UTF-8') as file:
            file.write(f"{get_formatted_time()} - не удалось найти заметок\n")
        return

    find_status = False

    if notes:
        for note in notes:
            if note["id"] == id:
                print(f"ID заметки: {note['id']}")
                print(f"Заголовок заметки: {note['title']}")
                print(f"Текст заметки: {note['text']}\n")
                find_status = True
                with open('log.txt', 'a', encoding='UTF-8') as file:
                    file.write(f"{get_formatted_time()} - просмотрена заметка под id: {id}\n")

    if find_status is False:
        print(f"Заметки под данным id: {id} не найдено\n")
        with open('log.txt', 'a', encoding='UTF-8') as file:
            file.write(f"{get_formatted_time()} - не удалось найти заметку под id: {id} для просмотра\n")


def delete_note(id):
    try:
        with open('notes.json', 'r', encoding='UTF-8') as file:
            notes = json.load(file)
    except FileNotFoundError:
        print("Нечего удалять когда заметок нет\n")
        with open('log.txt', 'a', encoding='UTF-8') as file:
            file.write(f"{get_formatted_time()} - не удалось найти заметок\n")
        return

    delete_status = False

    for i, note in enumerate(notes):
        if note["id"] == id:
            notes.pop(i)
            print("Заметка удалена\n")
            delete_status = True

            with open('notes.json', 'w', encoding='UTF-8') as file:
                json.dump(notes, file, ensure_ascii=False, indent=4)

            with open('log.txt', 'a', encoding='UTF-8') as file:
                file.write(f"{get_formatted_time()} - удалена заметка под id: {id}\n")

            break

    if delete_status is False:
        print(f"Заметки под данным id: {id} не найдено\n")
        with open('log.txt', 'a', encoding='UTF-8') as file:
            file.write(f"{get_formatted_time()} - не удалось найти заметку под id: {id} для удаления\n")


def show_notes():
    try:
        with open('notes.json', 'r', encoding='UTF-8') as file:
            notes = json.load(file)
    except FileNotFoundError:
        print("Нечего смотреть когда заметок нет\n")
        with open('log.txt', 'a', encoding='UTF-8') as file:
            file.write(f"{get_formatted_time()} - не удалось найти заметок\n")
        return

    for note in notes:
        print(f"ID заметки: {note['id']}")
        print(f"Заголовок заметки: {note['title']}")
        print(f"Текст заметки: {note['text']}\n")

    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(f"{get_formatted_time()} - просмотрен список заметок\n")


while True:
    print("1. Добавить заметку\n"
          "2. Посмотреть заметку по id\n"
          "3. Удалить заметку\n"
          "4. Просмотреть существующие заметки\n"
          "5. Выйти из программы\n")
    action = int(input("Введите номер действия: "))

    if action == 1:
        note_title = input("Введите заголовок заметки: ")
        note_text = input("Введите текст заметки: ")
        add_note(title=note_title, text=note_text)

    elif action == 2:
        id = int(input("Введите id нужной заметки: "))
        get_note(id)

    elif action == 3:
        id = int(input("Введите id нужной заметки: "))
        delete_note(id)

    elif action == 4:
        show_notes()

    elif action == 5:
        print("Завершение работы...")
        break

    else:
        print("Неверный выбор действия, попробуйте снова\n")