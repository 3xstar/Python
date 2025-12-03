import arcade
import arcade.utils
import random

SPACE_TEXTURE = ":resources:images/backgrounds/stars.png"
SPACESHIP_TEXTURE = ":resources:images/space_shooter/playerShip1_blue.png"
ENEMY_TEXTURE = ":resources:images/space_shooter/playerShip3_orange.png"
LASER_TEXTURE = ":resources:images/space_shooter/laserBlue01.png"
LOSE_MUSIC = ":resources:sounds/explosion1.wav"
WIN_MUSIC = ":resources:sounds/coin1.wav"
LASER_SOUND = ":resources:sounds/laser1.mp3"
BG_MUSIC = "background_music.mp3"

class Spaceship(arcade.Sprite):
    def __init__(self, pos_x, pos_y, scale, speed, health):
        super().__init__(SPACESHIP_TEXTURE, scale)
        self.center_x = pos_x
        self.center_y = pos_y
        self.health = health
        self.speed = speed
    def update(self):
        if self.health <= 0:
            self.kill()
    def get_damage(self, damage):
        self.health -= damage

class EnemySpaceship(arcade.Sprite):
    def __init__(self, pos_x, pos_y, scale, speed, health, window_height = 600):
        super().__init__(ENEMY_TEXTURE, scale)
        self.center_x = pos_x
        self.center_y = pos_y
        self.health = health
        self.speed = speed
        self.window_height = window_height
        self.turn_right(180)
        self.shoot_timer = 0

    def update(self):
        if self.health <= 0:
            self.kill()
        self.center_y -= self.speed

        if self.center_y <= - 20:
            self.center_y = self.window_height + random.randint(0, self.window_height)
    def get_damage(self, damage):
        self.health -= damage

class Laser(arcade.Sprite):
    def __init__(self, pos_x, pos_y, scale, speed, window_height, damage = random.randint(10, 20)):
        super().__init__(LASER_TEXTURE, scale, center_x=pos_x, center_y=pos_y)
        self.speed = speed
        self.window_height = window_height
        self.turn_right(-90)
        self.damage = damage
    def update(self):
        self.center_y += self.speed
        if self.center_y >= self.window_height + 50:
            self.kill()

class EnemyLaser(arcade.Sprite):
    def __init__(self, pos_x, pos_y, scale, speed, window_height, damage=5):
        super().__init__(LASER_TEXTURE, scale, center_x=pos_x, center_y=pos_y)
        self.speed = speed
        self.window_height = window_height
        self.damage = damage
        self.turn_right(90)  # Поворачиваем лазер вниз
    def update(self):
        self.center_y -= self.speed
        if self.center_y <= -50:
            self.kill()

class Game(arcade.Window):
    def __init__(self):
        super().__init__(title="Space Shooter")
        self.player_sprite = None
        self.laser_sprite = None
        self.enemy_sprite = None

        self.laser_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.enemy_laser_list = arcade.SpriteList()
        self.score = 0
        self.win_music = arcade.load_sound(WIN_MUSIC)
        self.lose_music = arcade.load_sound(LOSE_MUSIC)
        self.laser_sound = arcade.load_sound(LASER_SOUND)
        self.enemy_laser_sound = arcade.load_sound(LASER_SOUND)
        self.bg_music = arcade.load_sound(BG_MUSIC)
        self.bg_player = arcade.play_sound(self.bg_music, 0.2, looping=True)

    def setup(self):
        self.player_sprite = Spaceship(self.width / 2, self.height / 2, 0.5, 0.1, 100)
        self.enemy_generation(30)
        for enemy in self.enemy_list:
            enemy.shoot_timer = random.uniform(0, 1)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player_sprite.center_x = arcade.utils.lerp(self.player_sprite.center_x, x, self.player_sprite.speed)
        self.player_sprite.center_y = arcade.utils.lerp(self.player_sprite.center_y, y, self.player_sprite.speed)

    def on_update(self, delta_time: float):
        if self.player_sprite.health <= 0:
            return
        if len(self.enemy_list) == 0:
            return

        self.player_sprite.update()
        self.laser_list.update()
        self.enemy_list.update()
        self.enemy_laser_list.update()

        for enemy in self.enemy_list:
            enemy.shoot_timer += delta_time
            if enemy.shoot_timer >= 1.0:
                enemy.shoot_timer = 0
                laser = EnemyLaser(enemy.center_x, enemy.center_y, 0.3, 10, self.height)
                self.enemy_laser_list.append(laser)
                arcade.play_sound(self.enemy_laser_sound, 0.1)

        for enemy in self.enemy_list:
            shot_list = arcade.check_for_collision_with_list(enemy, self.laser_list)
            if shot_list:
                for laser in shot_list:
                    enemy.health -= laser.damage
                    laser.kill()

            collision = arcade.check_for_collision(enemy, self.player_sprite)
            if collision:
                enemy.kill()
                self.player_sprite.health -= 25

        player_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_laser_list)
        if player_hit_list:
            for laser in player_hit_list:
                self.player_sprite.health -= laser.damage
                laser.kill()

        if self.player_sprite.health <= 0:
            arcade.play_sound(self.lose_music, 0.1)

        if len(self.enemy_list) == 0:
            arcade.play_sound(self.win_music, 0.1)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2,
                                     self.height / 2,
                                     self.width,
                                     self.height,
                                     arcade.load_texture(SPACE_TEXTURE))
        self.player_sprite.draw()
        self.laser_list.draw()
        self.enemy_list.draw()
        self.enemy_laser_list.draw()

        arcade.draw_text(f"player health: {self.player_sprite.health}",
                        50, 50, arcade.color.WHITE, 14)
        arcade.draw_text(f"enemies count: {len(self.enemy_list)}",
                        50, 30, arcade.color.WHITE, 14)

        if self.player_sprite.health <= 0:
            arcade.draw_text("YOU LOSE", self.width / 2 - 125, self.height / 2,
                           arcade.color.RED, 40)

        if len(self.enemy_list) <= 0:
            arcade.draw_text("YOU WIN", self.width / 2 - 125, self.height / 2,
                           arcade.color.GREEN, 40)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT and self.player_sprite.health > 0:
            self.laser_sprite = Laser(self.player_sprite.center_x,
                                     self.player_sprite.center_y,
                                     0.3,
                                     10,
                                     self.height)
            self.laser_list.append(self.laser_sprite)
            arcade.play_sound(self.laser_sound, 0.1)

    def enemy_generation(self, count):
        for _ in range(count):
            self.enemy_sprite = EnemySpaceship(random.randint(10, self.width - 10),
                                             self.height + random.randint(10, self.height * 2),
                                             0.5,
                                             5,
                                             100,
                                             self.height * 2)
            self.enemy_list.append(self.enemy_sprite)

cosmo = Game()
cosmo.setup()
arcade.run()