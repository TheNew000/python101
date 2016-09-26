import potion
import random
import spell_class

class Hero(object):
    def __init__(self, name):
        self.name = name
        self.max_health = 25
        self.health = self.max_health
        self.magic_attack = 10
        self.attack_str = 5
        self.mana = 15
        self.special = 10
        self.inventory = [
            potion.Potion("Health Potion", "Health", 20),
            potion.Potion("Health Potion", "Health", 20),
            potion.Potion("Mana Potion", "Mana", 10)
        ]
        self.spells = [
            spell_class.Spell("Fireball", 10, 5),
            spell_class.Spell("Ice", 12, 6),
            spell_class.Spell("Lightning", 18, 8)
        ]

    def attack(self, dragon):
        print "You slashed him with your powerful sword!"
        dragon.health -= random.randrange(self.attack_str - 2, self.attack_str + 3) if self.health > 5 else random.randrange((self.attack_str * 2) - 2, (self.attack_str * 2) + 3)
        return True

    def use_potion(self):
        if len(self.inventory) > 0:
            print "You used a magical Potion or Lotion..."
            used_potion = self.inventory[0]
            used_potion.use(self)
            self.inventory.remove(used_potion)
            return True
        else:
            print "You don't have any potions left! Choose another Move!"
            return False

    def special_attack(self, dragon, menu):
        print "You have used a mighty AXE to slash the Dragon's underbelly!"
        dragon.health -= random.randrange((self.attack_str * 2) - 1, (self.attack_str * 2) + 4)
        if len(menu.options) > 4:
            menu.options.remove(menu.options[4])
        self.special -= 5
        return True
    
    def show_status(self):
        print '============================='
        print "Hero Name: ", self.name
        print "Hero Health: ", self.health
        print "Hero Mana: ", self.mana
        print '=============================\n'

