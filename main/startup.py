import pygame
from ui.menu.gamemenu import GameMenu


class StartUp:
    def __init__(self):
        display = pygame.display
        (width, height) = (1000, 1000)
        self.screen = display.set_mode((width, height))
        display.set_caption('Shining Force 2')
        self.gameMenu = GameMenu(self)
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.mainLoop = True

    def startUp(self):
        while self.mainLoop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.mainLoop = False
            self.gameMenu.run(self)
