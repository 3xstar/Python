import json

data = {
    "Nehorishiy chelovek": "Vadik",
    "age": 16,
    "uvlecheniya": "sleep, games, spisivat pod chistuyu >:("
}

add_data = {
    "interesi": "parit veipi"
}

with open("file.json", "w+", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

with open("file.json", "r+", encoding="utf-8") as file:
    new_data = json.load(file)
    # adaptive_data = [new_data, add_data]
    new_data.update(add_data)

with open("file.json", "w+", encoding="utf-8") as file:
    json.dump(new_data, file, ensure_ascii=False, indent=2)
    print(new_data)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)


user = User("Sasha", 16)
user.show_info()
print(user.__dict__)

with open(f"{user.name}.json", "w+", encoding="utf-8") as file:
    json.dump(user.__dict__, file, ensure_ascii=False, indent=2)


def dict_to_user(user):
    return User(user["name"], user["age"])


with open("Sasha.json", "r+", encoding="utf-8") as file:
    user = json
    user.show_info()
