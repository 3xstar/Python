import random
import arcade

#Создание окна игры
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=650, height=450, title="Ping-Pong")
        #Заготовки объектов
        self.ball = None
        self.platform1 = None
        self.platform2 = None
        self.spriteList = arcade.SpriteList()

        self.score1 = 0
        self.score2 = 0

    #Метод отрисовки
    def on_draw(self):
        self.clear() #Очистка экрана
        arcade.set_background_color(arcade.color.GRAY) #Цвет заднего фона
        self.spriteList.draw() #Отрисовка мяча

        arcade.draw_text(f"player 1: {self.score1}", 20, self.height - 30,
                         arcade.color.BLUE, 20)
        arcade.draw_text(f"player 2: {self.score2}", self.width - 130, self.height - 30,
                         arcade.color.RED, 20)

    #Обновление объектов на экране
    def on_update(self, delta_time: float):
        self.platform1.update()
        self.platform2.update()
        self.ball.update()

        if self.platform1.center_y < 0:
            self.platform1.center_y = self.height
        if self.platform1.center_y > self.height:
            self.platform1.center_y = 0

        if self.platform2.center_y < 0:
            self.platform2.center_y = self.height
        if self.platform2.center_y > self.height:
            self.platform2.center_y = 0

        if self.ball.center_x < 0:
            self.ball.change_x = -self.ball.change_x
            self.score2 += 1
            self.restart()

        if self.ball.center_x > self.width:
            self.ball.change_x = -self.ball.change_x
            self.score1 += 1
            self.restart()

        if self.ball.center_y < 0:
            self.ball.change_y = -self.ball.change_y
        if self.ball.center_y > self.height:
            self.ball.change_y = -self.ball.change_y

        platform1_collision = arcade.check_for_collision(self.platform1, self.ball)
        platform2_collision = arcade.check_for_collision(self.platform2, self.ball)

        if platform1_collision:
            self.ball.change_x = -self.ball.change_x
            self.ball.change_y = self.ball.change_y + self.platform1.change_y / 2 + random.randint(-1, 1)

        if platform2_collision:
            self.ball.change_x = -self.ball.change_x
            self.ball.change_y = self.ball.change_y + self.platform2.change_y / 2 + random.randint(-1, 1)

        if self.ball.change_y > 5:
            self.ball.change_y -= 0.1

    #Метод для реагирования нажатий на клавиши
    def on_key_press(self, symbol: int, modifiers: int): #Symbol - нажатая клавиша
        if symbol == arcade.key.W:
            self.platform1.change_y = 2
        if symbol == arcade.key.S:
            self.platform1.change_y = -2

        if symbol == arcade.key.UP:
            self.platform2.change_y = 2
        if symbol == arcade.key.DOWN:
            self.platform2.change_y = -2

    # def on_key_release(self, symbol: int, modifiers: int):
    #     if symbol == arcade.key.W or symbol == arcade.key.S:
    #         self.platform1.change_y = 0
    #
    #     if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
    #         self.platform2.change_y = 0

    def setup(self):
        #Создание объектов
        self.ball = arcade.Sprite(":resources:images/pinball/pool_cue_ball.png",
                                  center_x=self.width/2,
                                  center_y=self.height/2,
                                  scale=0.3)
        self.platform1 = arcade.Sprite(":resources:images/tiles/bridgeB.png",
                                       center_x= 80,
                                       center_y=self.height/2,
                                       angle=90,
                                       scale=0.7)
        self.platform2 = arcade.Sprite(":resources:images/tiles/bridgeB.png",
                                       center_x= self.width-80,
                                       center_y=self.height/2,
                                       angle=-90,
                                       scale=0.7)
        self.spriteList.append(self.ball)
        self.spriteList.append(self.platform1)
        self.spriteList.append(self.platform2)
        self.ball.change_x = 4

    def restart(self):
        self.platform1.center_y = self.height/2
        self.platform2.center_y = self.height / 2
        self.ball.center_x = self.width / 2
        self.ball.center_y = self.height / 2
        self.ball.change_y = 0

#Запуск игры
ping_pong = Game()
ping_pong.setup()
arcade.run()