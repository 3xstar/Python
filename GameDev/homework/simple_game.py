import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Влево / вправо"

player_texture = arcade.load_texture(":resources:images/enemies/slimeBlock.png")
PLAYER_SPEED = 10

class Player(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(texture=player_texture, scale = 0.5)
        self.center_x = x
        self.center_y = y

    def update(self, keys):
        if keys["left"] and self.center_x > self.width / 2:
            self.center_x -= PLAYER_SPEED
        if keys["right"] and self.center_x < SCREEN_WIDTH - self.width / 2:
            self.center_x += PLAYER_SPEED

class CatchGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.player = None
        self.objects = None
        self.keys = {"left": False, "right": False}

    def setup(self):
        self.player = Player(SCREEN_WIDTH // 2, 40)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def on_update(self, delta_time):
        self.player.update(self.keys)

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
