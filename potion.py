class Potion(object):
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

    def use(self, hero):
        if self.type == "Health":
            print "You have restored your HEALTH!"
            hero.health += self.power
            if hero.health > hero.max_health:
                hero.health = hero.max_health
            return True
        elif self.type == "Mana":
            print "Your mana has been restored!"
            hero.mana += self.power
            return True
