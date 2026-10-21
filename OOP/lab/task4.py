class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.attack_status = False
        self.alive = True


    def attack(self, character):
        if character.alive is True:
            print(f"{character.name} подготовил атаку")
            character.attack_status = True
        else:
            print(f"{character.name} мертв и не может сражаться")

    def take_damage(self, character1, character2):
        if character1.alive is True and character2.alive is True:
            if character1.attack_status:
                character2.hp -= character1.damage
                print(f"{character1.name} нанес удар персонажу {character2.name}")
                if character2.hp <= 0:
                    print(f"{character2.name} умер в бою, {character1.name} победил")
                    character2.alive = False
            else:
                print(f"{character1.name} замахнулся на персонажа {character2.name}, "
                      f"но не смог провести атаку так как был не готов")
        else:
            print("Один из персонажей умер, бой окончен")

    def is_alive(self, character):
        if character.alive is True:
            print(f"Персонаж {character.name} жив")
        else:
            print(f"Персонаж {character.name} мертв")

warrior = Character("Воин", 300, 50)
mage = Character("Маг", 250, 60)
while warrior.alive and mage.alive:
    warrior.attack(warrior)
    mage.attack(mage)
    warrior.take_damage(warrior, mage)
    mage.take_damage(mage, warrior)
    warrior.is_alive(warrior)
    mage.is_alive(mage)
else:
    print("Игра окончена")

