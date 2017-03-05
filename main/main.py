import pygame

from core.menu.gamemenu import GameMenu
pygame.init()
display = pygame.display
(width, height) = (1000, 1000)
screen = display.set_mode((width, height))
display.set_caption('Shining Force 2')
backgroundColor = (255, 255, 255)
screen.fill(backgroundColor)
gameMenu = GameMenu(screen)
gameMenu.run()
