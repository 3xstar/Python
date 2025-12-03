import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Поймай падающие объекты"

OBJECT_COUNT = 5
OBJECT_SPEED = 5
BASKET_SPEED = 10
START_SCORE = 10

basket_texture = arcade.load_texture(":resources:images/enemies/slimeBlock.png")
gold_texture = arcade.load_texture(":resources:images/items/coinGold.png")
silver_texture = arcade.load_texture(":resources:images/items/coinSilver.png")
bronze_texture = arcade.load_texture(":resources:images/items/coinBronze.png")

items = [gold_texture, silver_texture, bronze_texture]

class Basket(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(texture=basket_texture, scale = 0.5)
        self.center_x = x
        self.center_y = y

    def update(self, keys):
        if keys["left"] and self.center_x > self.width / 2:
            self.center_x -= BASKET_SPEED
        if keys["right"] and self.center_x < SCREEN_WIDTH - self.width / 2:
            self.center_x += BASKET_SPEED


class FallingObject(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(texture=items[random.randint(0,2)], scale=0.5)
        self.center_x = x
        self.center_y = y

    def update(self):
        self.center_y -= OBJECT_SPEED
        if self.center_y < 0:
            self.reset_position()

    def reset_position(self):
        self.center_x = random.randint(20, SCREEN_WIDTH - 20)
        self.center_y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 200)


class CatchGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.basket = None
        self.objects = None
        self.score = START_SCORE
        self.keys = {"left": False, "right": False}

    def setup(self):
        self.basket = Basket(SCREEN_WIDTH // 2, 40)
        self.objects = arcade.SpriteList()
        for _ in range(OBJECT_COUNT):
            x = random.randint(20, SCREEN_WIDTH - 20)
            y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 200)
            self.objects.append(FallingObject(x, y))

    def on_draw(self):
        arcade.start_render()
        self.basket.draw()
        self.objects.draw()
        arcade.draw_text(f"Очки: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.BLACK, 20)

    def on_update(self, delta_time):
        self.basket.update(self.keys)
        self.objects.update()

        for obj in self.objects:
            if arcade.check_for_collision(self.basket, obj):
                obj.reset_position()
                self.score += 1

        for obj in self.objects:
            if obj.center_y < 0:
                obj.reset_position()
                self.score -= 1

        if self.score <= 0:
            arcade.close_window()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.keys["left"] = True
        elif key == arcade.key.RIGHT:
            self.keys["right"] = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.keys["left"] = False
        elif key == arcade.key.RIGHT:
            self.keys["right"] = False

game = CatchGame()
game.setup()
arcade.run()
