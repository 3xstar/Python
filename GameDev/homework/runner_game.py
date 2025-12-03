import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Runner Game"

PLAYER_SCALING = 0.5
OBSTACLE_SCALING = 0.5

PLAYER_SPEED = 5
GRAVITY = 1
JUMP_SPEED = 20

obstacle_texture = ":resources:images/tiles/bomb.png"
obstacle2_texture = ":resources:images/tiles/boxCrate_double.png"
obstacle3_texture = ":resources:images/tiles/brickTextureWhite.png"
ground_texture = ":resources:images/tiles/grassMid.png"

obstacles = [obstacle_texture, obstacle2_texture, obstacle3_texture]

class Player(arcade.AnimatedTimeBasedSprite):
    def __init__(self):
        super().__init__(scale=PLAYER_SCALING)
        self.center_x = 100
        self.center_y = 150
        self.setup_animation()

    def setup_animation(self):
        # Загружаем текстуры для анимации ходьбы
        for i in range(8):
            texture = arcade.load_texture(
                f":resources:images/animated_characters/male_adventurer/maleAdventurer_walk{i}.png")
            frame = arcade.AnimationKeyframe(i, 100, texture)
            self.frames.append(frame)

        # Устанавливаем начальную текстуру
        self.texture = self.frames[0].texture if self.frames else None
        self.cur_frame_idx = 0

class Obstacle(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(obstacles[random.randint(0,2)], OBSTACLE_SCALING - 0.2)
        self.center_x = x
        self.center_y = y

class Ground(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(ground_texture, OBSTACLE_SCALING)
        self.center_x = x
        self.center_y = y


class RunnerGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.player_list = None
        self.obstacle_list = None
        self.ground_list = None

        self.player_sprite = None
        self.physics_engine = None

        self.score = 0

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.obstacle_list = arcade.SpriteList()
        self.ground_list = arcade.SpriteList( )

        self.player_sprite = Player()
        self.player_list.append(self.player_sprite)

        self.ground_generation(0, 100, 20)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.ground_list, gravity_constant=GRAVITY)

        for _ in range(3):
            x = random.randint(400, SCREEN_WIDTH)
            y = 150
            obstacle = Obstacle(x, y)
            self.obstacle_list.append(obstacle)

    def on_draw(self):
        arcade.start_render()

        self.player_list.draw()
        self.ground_list.draw()
        self.obstacle_list.draw()

        arcade.draw_text(f"Score: {self.score}",
                         10,
                         10,
                         arcade.color.BLACK,
                         20
        )

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.player_sprite.update_animation(delta_time)

        for obstacle in self.obstacle_list:
            obstacle.center_x -= PLAYER_SPEED
            if obstacle.center_x < 0:
                obstacle.center_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)

        for ground in self.ground_list:
            ground.center_x -= PLAYER_SPEED
            if ground.center_x < - 64:
                ground.center_x = SCREEN_WIDTH + 64

        if arcade.check_for_collision_with_list(self.player_sprite, self.obstacle_list):
            arcade.close_window()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.physics_engine.can_jump():
            self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.player_sprite.change_x = 0

    def ground_generation(self, x, y, n):
        for i in range(n):
            tile = Ground(x + (i * 64), y)
            self.ground_list.append(tile)


if __name__ == "__main__":
    game = RunnerGame()
    game.setup()
    arcade.run()