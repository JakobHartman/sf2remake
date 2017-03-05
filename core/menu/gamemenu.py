import pygame
from .menuitem import MenuItem
from ui.image import Image
from audio.musicloader import MusicLoader


class GameMenu:
    def __init__(self, screen):
        self.screen = screen
        self.scrWidth = self.screen.get_rect().width
        self.scrHeight = self.screen.get_rect().height
        self.clock = pygame.time.Clock()
        items = ('New Game', 'Continue', 'Delete Save', 'Quit Game')
        self.items = []
        self.createMenuItems(items)
        self.mainImage = Image("menu/s2_Logo.png", (700, 400), (self.scrWidth / 6, 0))
        MusicLoader.loadMusic("menu/Battle2.mp3")
        MusicLoader.play()

    def run(self):
        mainLoop = True
        while mainLoop:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainLoop = False

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.mainImage.image, self.mainImage.pos)

            for item in self.items:
                mpos = pygame.mouse.get_pos()
                if item.isMouseSelection(mpos):
                    item.setFontSize(35)
                    item.set_italic(False)
                else:
                    item.setFontSize(30)
                    item.set_italic(False)

                if item.isMouseClicked(mpos, pygame.mouse.get_pressed()):
                    item.setFontColor((255, 0, 0))
                    if item.text == "Quit Game":
                        mainLoop = False
                else:
                    item.setFontColor((255, 255, 255))
                self.repoMenuItems()
                self.screen.blit(item.label, item.position)

            pygame.display.flip()

    def createMenuItems(self, items):

        for index, item in enumerate(items):
            menuItem = MenuItem(item, "C:\Windows\Fonts\Arial.ttf", 30, (255, 255, 255), 0, 0)
            t_h = len(items) * menuItem.height
            posx = (self.scrWidth / 2) - (menuItem.width / 2)
            posy = (self.scrHeight / 2) - (t_h / 2) + ((index * 2) + index * menuItem.height)
            menuItem.setPosition(posx, posy)
            self.items.append(menuItem)

    def repoMenuItems(self):
        for index, item in enumerate(self.items):
            t_h = len(self.items) * item.height
            posx = (self.scrWidth / 2) - (item.width / 2)
            posy = (self.scrHeight / 2) - (t_h / 2) + ((index * 2) + index * item.height)
            item.setPosition(posx, posy)
            item.render(item.text, True, item.font_color)
