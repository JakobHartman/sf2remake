from .unit import Unit


class Monster(Unit):
    def __init__(self, gold, specialMoves, name, hp, at, df, ag, mv, weapon, spells, inventory):
        super().__init__(name, hp, at, df, ag, mv, weapon, spells, inventory)
        self.gold = gold
        self.specialMoves = specialMoves
