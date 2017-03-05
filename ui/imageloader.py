import pygame


class ImageLoader:

    @staticmethod
    def load(imagePath, pos):
        x,y = pos
        image = pygame.image.load(imagePath)
        image = pygame.transform.scale(image, (x,y))
        return image
