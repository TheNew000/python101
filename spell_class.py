class Spell:
    def __init__(self, name, power, mana_cost):
        self.name = name
        self.power = power
        self.mana_cost = mana_cost

    def fire(self, user, target):
        print self.name
        if user.mana >= self.mana_cost:
            print "%s used the spell %s" % (user.name, self.name)
            user.mana -= self.mana_cost
            target.health -= self.power
            return True
        else:
            print "%s doesn't have enough mana to use this spell! Choose another move!" % user.name
            return False
