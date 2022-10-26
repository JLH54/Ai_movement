# This Python file uses the following encoding: utf-8
import sys
import pygame
import Ai
from PySide6.QtWidgets import QApplication, QWidget,QComboBox
from PySide6.QtCore import QTimer

class Timer:
    _clock = None
    _dt:float = 0.016

    def __init__(self):
        self._clock = pygame.time.Clock()

    def update(self):
        self._dt = self._clock.tick(60)/1000

    def get_deltaTime(self):
        return self._dt

class Game:
    black = (0, 0 ,0)
    width:int
    height:int
    state = 0
    def __init__(self):
        pygame.init()
        self.gameInit()
        self.ai = Ai
        self.timer = Timer()
        self.width= 1000 / 8
        self.height = 720 / 8
        self.should_quit = False
        self.up_key_pressed = False
        self.down_key_pressed = False

    def loop(self):
        self.timer.update()
        dt = self.timer.get_deltaTime()
        print(self.state)
        self.process_input()
        self.gameLogic(dt)
        self.render()

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.should_quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.up_key_pressed = True
                if event.key == pygame.K_s:
                    self.down_key_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.up_key_pressed = False
                if event.key == pygame.K_s:
                    self.down_key_pressed = False

    def gameInit(self):
        self.size = self.width, self.height = 1000, 720
        self.src = pygame.display.set_mode([700,520])

        self.screen = pygame.display.set_mode(self.size)

    def gameLogic(self, dt):
        #ai behaviour
        pass

    def render(self):
        self.screen.fill(self.black)
        pygame.display.flip()

class Window(QWidget):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.initUi()
        self.init_pygame(self.game)


    def init_pygame(self, game):
        self.game = game
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(0)

    def pygame_loop(self):
        if self.game.loop():
            self.close()

    def initUi(self):
        self.setWindowTitle("")
        self.setGeometry(0,400,300,200)

        #settings for ai
        self.cbAi = QComboBox(self)
        self.cbAi.move(100,75)
        self.cbAi.addItem("Seek")
        self.cbAi.addItem("Flee")
        self.cbAi.addItem("Wander")
        self.cbAi.activated.connect(self.activated)

        self.show()

    def activated(self, index):
        print("Current state : ", index)
        self.game.state = index


def main():
    app = QApplication(sys.argv)
    game = Game()
    exe = Window(game)

    app.setActiveWindow(exe)
    # ...
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
