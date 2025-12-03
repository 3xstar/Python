import random
class Warrior:

    def __init__(self, hp, damage, armor, mana):
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.mana = mana

    def shield(self, enemy):
        print("Восстановление")
        self.armor *= 0.12 * self.armor
        self.hp += self.hp * 0.12
        # if enemy.damage > self.armor:
        #     print("Сработала защита, урон прошел")
        #     self.hp -= enemy.damage / 2
        # else:
        #     print("Сработала защита, урон не прошел")

    def give_damage(self, enemy):
        if self.damage > enemy.armor:
            print("Урон прошел")
            enemy.hp -= self.damage
        else:
            print("Урон не прошел")
            enemy.hp -= self.damage / 5

        enemy.armor -= enemy.damage / 2
    def pass_game(self):
        self.hp = 0


class Knight(Warrior):
    def __init__(self, hp, damage, armor, stamina, name, mana=0):
        super().__init__(hp, damage, armor, mana)
        self.stamina = stamina
        self.name = name
        self.is_shield = False
        self.pelmeshi_chance = 100

    def action_menu(self, enemy):
        print("1. Ударить мечом",
              "\n2. Поставить щит",
              "\n3. Сдаться")
        action = int(input("Введите номер действия: "))
        match action:
            case 1:
                self.give_damage(enemy)
                if (random.randint(1, 100)) < self.pelmeshi_chance:
                    self.give_pelemeski()
            case 2:
                self.shield(enemy)
                self.is_shield = True
            case 3:
                self.pass_game()

    def show_stats(self):
        print(f"Имя: {self.name}",
              f"Урон: {self.damage}",
              f"Защита: {self.armor}",
              f"Выносливость: {self.stamina}",
              f"Жизни: {self.hp}")

    def give_pelemeski(self):
        print("Сработали пельмешки")
        action = random.randint(1,3)
        if action == 1:
            print("Восстановление здоровья")
            self.hp += 0.5 * self.hp
        if action == 2:
            print("Восстановление выносливости")
            self.stamina += 0.5 * self.stamina
        if action == 3:
            print("Восстановление брони")
            self.armor += 0.5 * self.armor


hero_one = Knight(500, 200, 100, 100, "ZACHAR ORG K")
hero_two = Knight(400, 200, 100, 150, "DMITRIY G.")

while True:
    hero_one.show_stats()
    hero_two.show_stats()

    print(f"Ходит {hero_one.name}")
    hero_one.action_menu(hero_two)
    if hero_two.hp <= 0:
        print(f"{hero_two.name} умер")
        break

    print(f"Ходит {hero_two.name}")
    hero_two.action_menu(hero_one)
    if hero_one.hp <= 0:
        print(f"{hero_one.name} умер")
        break