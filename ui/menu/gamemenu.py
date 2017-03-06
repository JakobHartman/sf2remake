import pygame
from .menuitem import MenuItem
from ui.image import Image
from audio.musicloader import MusicLoader


class GameMenu:
    def __init__(self, parent):
        self.scrWidth = parent.screen.get_rect().width
        self.scrHeight = parent.screen.get_rect().height
        self.items = []
        self.createMenuItems(('New Game', 'Continue', 'Options', 'Quit Game'))
        self.mainImage = Image("menu/s2_Logo.png", (700, 400), (self.scrWidth / 6, 0))
        MusicLoader.loadMusic("menu/Battle2.mp3")
        MusicLoader.play(True)



    def run(self, parent):
        parent.screen.fill((0, 0, 0))
        parent.screen.blit(self.mainImage.image, self.mainImage.pos)

        for item in self.items:
            mpos = pygame.mouse.get_pos()
            if item.isMouseSelection(mpos):
                item.setFontSize(35)
                item.set_italic(False)
            else:
                item.setFontSize(30)
                item.set_italic(True)

            if item.isMouseClicked(mpos, pygame.mouse.get_pressed()):
                item.setFontColor((255, 0, 0))
                if item.text == "Quit Game":
                    parent.mainLoop = False
            else:
                item.setFontColor((255, 255, 255))
            parent.screen.blit(item.label, item.position)

        pygame.display.flip()

    def createMenuItems(self, items):
        for index, item in enumerate(items):
            menuItem = MenuItem(item, "C:\Windows\Fonts\Arial.ttf", 30, (255, 255, 255), 0, 0)
            t_h = len(items) * menuItem.height
            posx = (self.scrWidth / 2) - (menuItem.width / 2)
            posy = (self.scrHeight / 2) - (t_h / 2) + ((index * 2) + index * menuItem.height)
            menuItem.setPosition(posx, posy)
            self.items.append(menuItem)
