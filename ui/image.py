from .imageloader import ImageLoader
import os


class Image:
    def __init__(self, filename, dim, pos):
        w,h = dim
        x, y = pos
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, "../assets/images/" + filename)
        self.image = ImageLoader.load(filename, (w, h))
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)



