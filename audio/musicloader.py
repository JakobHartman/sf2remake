import pygame
import os

class MusicLoader:
    @staticmethod

    def loadMusic(file):
        pygame.mixer.init()
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "../assets/music/" + file)
        music = pygame.mixer.music.load(filename)
        return music
    @staticmethod
    def play():
        pygame.mixer.music.play(1,1)