import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Собери как можно больше монеток!"

OBJECT_COUNT = 5
OBJECT_SPEED = 5
PLAYER_SPEED = 10
START_SCORE = 10

player_texture = arcade.load_texture(":resources:images/enemies/fly.png")
gold_texture = arcade.load_texture(":resources:images/items/coinGold.png")
silver_texture = arcade.load_texture(":resources:images/items/coinSilver.png")
bronze_texture = arcade.load_texture(":resources:images/items/coinBronze.png")
bg_texture = ":resources:images/backgrounds/stars.png"

items = [gold_texture, silver_texture, bronze_texture]

class Player(arcade.Sprite):
    def __init__(self, x, y, speed):
        super().__init__(texture=player_texture, scale = 0.5)
        self.center_x = x
        self.center_y = y
        self.speed = speed


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


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player = None
        self.objects = None
        self.score = START_SCORE

    def setup(self):
        self.player = Player(SCREEN_WIDTH // 2, 40, 1)
        self.objects = arcade.SpriteList()
        for _ in range(OBJECT_COUNT):
            x = random.randint(20, SCREEN_WIDTH - 20)
            y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 200)
            self.objects.append(FallingObject(x, y))

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player.center_x = arcade.utils.lerp(self.player.center_x, x, self.player.speed)
        self.player.center_y = arcade.utils.lerp(self.player.center_y, y, self.player.speed)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2,
                                      self.height / 2,
                                      self.width,
                                      self.height,
                                      arcade.load_texture(bg_texture))
        self.player.draw()
        self.objects.draw()
        arcade.draw_text(f"Очки: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)

    def on_update(self, delta_time):
        self.player.update()
        self.objects.update()

        for obj in self.objects:
            if arcade.check_for_collision(self.player, obj):
                obj.reset_position()
                self.score += 1

        for obj in self.objects:
            if obj.center_y < 0:
                obj.reset_position()
                self.score -= 1

        if self.score <= 0:
            arcade.close_window()

game = Game()
game.setup()
arcade.run()
