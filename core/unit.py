class Unit(object):
    spells = []

    def __init__(self, name, hp, at, df, ag, mv, weapon, spells, inventory, mvType):
        self.name = name
        self.hp = hp
        self.at = at
        self.df = df
        self.ag = ag
        self.mv = mv
        self.weapon = weapon
        self.spells = spells
        self.inventory = inventory
        self.mvType = mvType