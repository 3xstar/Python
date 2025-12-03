# "Лабиринт" Захар/Лера
# - Механика: Игрок (круг) должен дойти до выхода (зелёный квадрат), избегая стен (линии).
# - Управление: WASD или стрелки.
# - Усложнение: Добавить врагов (движущиеся точки).

import arcade
import random

from arcade.color import GREEN, RED

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

player_texture = ":resources:images/pinball/bumper.png"
exit_texture = ":resources:images/enemies/slimeBlock.png"
wall_texture = "wall.png"
enemy_texture = ":resources:images/pinball/pool_cue_ball.png"
bg_texture = "bg.png"
bg_music = "background_music.mp3"

wall_positions = [180, 90]

class Player(arcade.Sprite):
    def __init__(self, x, y, health, speed):
        super().__init__(player_texture, scale=0.3)
        self.center_x = x
        self.center_y = y
        self.health = health
        self.speed = speed
        self.game_over = False
        self.game_won = False

    def update(self):
        if self.health <= 0:
            self.kill()
            self.game_over = True
        if self.game_over or self.game_won:
            return

    def get_damage(self, damage):
        self.health -= damage

class Enemy(arcade.Sprite):
    def __init__(self, x, y, speed, window_height = 600):
        super().__init__(enemy_texture, scale=0.3)
        self.center_x = x
        self.center_y = y
        self.speed = speed
        self.window_height = window_height

class Wall(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(wall_texture, scale=0.12)
        self.center_x = x
        self.center_y = y
        self.turn_right(wall_positions[random.randint(0, 1)])

class Exit(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(exit_texture, scale=0.3)
        self.center_x = x
        self.center_y = y

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title="Labyrinth")
        self.player_sprite = None
        self.enemy_sprite = None
        self.wall_sprite = None
        self.exit_sprite = None
        self.physics_engine = None
        self.game_active = True

        self.wall_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bg_music = arcade.load_sound(bg_music)
        self.bg_player = arcade.play_sound(self.bg_music, 0.2, looping=True)

    def setup(self):
        self.player_sprite = Player(self.width / 2, self.height / 12, 100, 0.1)
        self.exit_sprite = Exit(self.width / 2, self.height - 10)
        self.enemy_generation(30)
        self.wall_generation(80)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if not self.game_active:
            return

        self.player_sprite.center_x = arcade.utils.lerp(self.player_sprite.center_x, x, self.player_sprite.speed)
        self.player_sprite.center_y = arcade.utils.lerp(self.player_sprite.center_y, y, self.player_sprite.speed)

        self.physics_engine.update()

    def on_update(self, delta_time: float):
        if not self.game_active:
            return

        self.player_sprite.update()
        self.enemy_list.update()
        self.wall_list.update()
        self.exit_sprite.update()

        for enemy in self.enemy_list:
            collision = arcade.check_for_collision(enemy, self.player_sprite)
            if collision:
                enemy.kill()
                self.player_sprite.health -= 10

        exit_collision = arcade.check_for_collision(self.player_sprite, self.exit_sprite)
        if exit_collision:
            self.player_sprite.game_won = True
            self.game_active = False

        if self.player_sprite.game_over:
            self.game_active = False

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2,
                                      self.height / 2,
                                      self.width,
                                      self.height,
                                      arcade.load_texture(bg_texture))
        self.player_sprite.draw()
        self.enemy_list.draw()
        self.wall_list.draw()
        self.exit_sprite.draw()

        arcade.draw_text(f"PLAYER HEALTH: {self.player_sprite.health}",
                         50, 550, arcade.color.GREEN, 20)

        if self.player_sprite.game_over:
            arcade.draw_text("YOU LOSE", self.width / 2 - 125, self.height / 2, font_size=40, color=RED)
            self.game_active = False

        if self.player_sprite.game_won:
            arcade.draw_text("YOU WIN", self.width / 2 - 125, self.height / 2, font_size=40, color=GREEN)
            self.game_active = False

    def enemy_generation(self, count):
        for _ in range(count):
            self.enemy_sprite = Enemy(random.randint(10, self.width - 10),
                                               random.randint(10, self.height - 10),5, self.height * 2)
            self.enemy_list.append(self.enemy_sprite)

    def wall_generation(self, count):
        for _ in range(count):
            self.wall_sprite = Wall(random.randint(10, self.width - 10),
                                               random.randint(10, self.height - 10))
            self.wall_list.append(self.wall_sprite, )

labyrinth = Game()
labyrinth.setup()
arcade.run()

