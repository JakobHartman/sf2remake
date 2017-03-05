import pygame

pygame.init()


class MenuItem(pygame.font.Font):
    def __init__(self, text, font, font_size, font_color, posy, posx):
        self.font = font;
        super().__init__(font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, True, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.posx = posx
        self.posy = posy
        self.position = posx, posy

    def setPosition(self, x, y):
        self.position = (x, y)
        self.posx = x
        self.posy = y

    def setFontColor(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)

    def setFontSize(self, size):
        super().__init__(self.font, size)
        self.label = self.render(self.text, True, self.font_color)

    def isMouseSelection(self, pos):
        x, y = pos
        if (x >= self.posx and x <= self.posx + self.width) and \
                (y >= self.posy and y <= self.posy + self.height):
            return True
        return False

    def isMouseClicked(self, pos, clicked):
        isHovered = self.isMouseSelection(pos)
        if isHovered and clicked[0]:
            return True
        else:
            return False
