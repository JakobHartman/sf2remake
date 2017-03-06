from .unit import Unit


class Character(Unit):
    def __init__(self, lv, cClass, promotions, name, hp, at, df, ag, mv, weapon, spells, inventory):
        super().__init__(name, hp, at, df, ag, mv, weapon, spells, inventory)
        self.cClass = cClass
        self.lv = lv
        self.promotions = promotions
        self.xp = 0


    def levelUp(self):
        self.lv += 1
        ##need to calculate the new level stats

    def addXP(self, xp):
        self.xp += xp
        if xp > 100:
            self.levelUp()
