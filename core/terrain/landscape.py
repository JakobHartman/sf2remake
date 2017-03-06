from ui.imageloader import ImageLoader


class LandScape:
    def __init__(self, lType, effects, mvMod, image):
        w, c, a, m, f, h, s, e = effects
        wm, cm, am, mm, fm, hm, sm, em = mvMod
        self.percents = (w, c, a, m, f, h, s, e)
        self.mods = (wm, cm, am, mm, fm, hm, sm, em)
        self.lType = lType
        self.image = ImageLoader.load(image, (16, 16))

    @staticmethod
    def sky():
        return LandScape("Sky", (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 1, 0, 0),"")

    @staticmethod
    def even():
        return LandScape("Even Ground", (15, 15, 15, 15, 0, 15, 0, 15), (1, 1, 1, 1, 1, 1, 0, 1),"")

    @staticmethod
    def pathsBridge():
        return LandScape("Path/Bridge", (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 1, 0, 0),"")

    @staticmethod
    def overgrowth():
        return LandScape("Overgrowth", (30, 30, 30, 30, 0, 30, 0, 30), (1.5, 1.5, 1, 1, 1, 1, 0, 1),"")

    @staticmethod
    def forest():
        return LandScape("Forest", (30, 30, 30, 30, 0, 30, 0, 30), (2, 2.5, 1, 1.5, 1, 1, 0, 1),"")

    @staticmethod
    def mountains():
        return LandScape("Mountains", (30, 30, 30, 30, 0, 30, 0, 30), (1.5, 2.5, 1, 1.5, 1, 1, 0, 1),"")

    @staticmethod
    def sand():
        return LandScape("Sand", (0, 0, 0, 0, 0, 0, 0, 0), (1.5, 2.5, 2, 1.5, 1, 1, 0, 2),"")

    @staticmethod
    def hMountain():
        return LandScape("High Mountain", (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 1, 0, 0),"")

    @staticmethod
    def water():
        return LandScape("Water", (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 1, 1, 0),"")

    @staticmethod
    def nothing(filename):
        return LandScape("Nothing", (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0),filename)


    @staticmethod
    def getTerrain(tType, filename):
        if tType == 0:
            return LandScape.sky()
        if tType == 1:
            return LandScape.even()
        if tType == 2:
            return LandScape.pathsBridge()
        if tType == 3:
            return LandScape.overgrowth()
        if tType == 4:
            return LandScape.forest()
        if tType == 5:
            return LandScape.mountains()
        if tType == 6:
            return LandScape.sand()
        if tType == 7:
            return LandScape.hMountain()
        if tType == 8:
            return LandScape.water()
        if tType == 9:
            return LandScape.nothing(filename)