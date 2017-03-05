class Unit(object):
    spells = []

    def __init__(self, name, hp, at, df, ag, mv, weapon, spells, inventory):
        self.name = name
        self.hp = hp
        self.at = at
        self.df = df
        self.ag = ag
        self.mv = mv
        self.weapon = weapon
        self.spells = spells
        self.inventory = inventory

    def getName(self):
        return self.name

    def getHP(self):
        return self.hp

    def getAT(self):
        return self.at

    def getDF(self):
        return self.df

    def getAG(self):
        return self.ag

    def getMV(self):
        return self.mv

    def getWeapon(self):
        return self.weapon

    def getSpell(self, pos):
        return self.spells[pos]

    def getSpells(self):
        return self.spells

    def getItem(self, pos):
        return self.inventory[pos]

    def setName(self, name):
        self.name = name

    def setHP(self, hp):
        self.hp = hp

    def setAT(self, at):
        self.at = at

    def setDF(self, df):
        self.df = df

    def setAG(self, ag):
        self.ag = ag

    def setMV(self, mv):
        self.mv = mv

    def setWeapon(self, weapon):
        self.weapon = weapon

    def addSpell(self, spell):
        self.spells.append(spell)

    def setItem(self, item, pos):
        self.inventory[pos] = item
