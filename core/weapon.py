from .item import Item


class Weapon(Item):
    def __init__(self, name, able, at, val, wType, special):
        super().__init__(name, able)
        self.at = at
        self.val = val
        self.special = special
        self.wType = wType
