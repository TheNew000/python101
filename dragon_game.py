import random
from dragon_class import Dragon
from hero_class import Hero
import menu_class
import subprocess
import spell_class

hero = Hero(raw_input("You've encountered a dragon!!!  Tell us your name!    "))
dragon = Dragon()


main_menu = menu_class.Menu([
    menu_class.Option("Fight", lambda: hero.attack(dragon)),
    menu_class.Option("Use Item", lambda: get_input(item_menu)),
    menu_class.Option("Use Spell", lambda: get_input(spell_menu)),
    menu_class.Option("Flee", lambda: flee())
])

spell_menu = menu_class.Menu([
    menu_class.Option("Go Back", lambda: get_input(main_menu))
    ])
item_menu = menu_class.Menu([
    menu_class.Option("Go Back", lambda: get_input(main_menu))
    ])

def flee():
    print "You flee you COWARD!!  CHICKENBUTT!!"
    play_again = raw_input("Want to play again? [Y/N]\n".upper())
    if play_again == "Y" or play_again == "y":
        subprocess.call(['python', 'dragon_game.py'])
    else:
        exit(0)

def start_game(): 
    print "         ^                        ^"
    print "         |\      \        /      /|"
    print "        /  \     |\__  __/|     /  \ "
    print "       / /\ \    \ _ \/ _ /    /    \ "
    print "      / / /\ \    {*}\/{*}    /  / \ \ "
    print "     | | |  \ \   ( (00) )   /  // |\ \ "
    print "     | | |  |\ \  /(WWWW)\  /  / | || \| "
    print "     | | |  | \|  \(^^^^)/ /  / || || || "
    print "    / / /   | |  (_______\/  /| || || ||"
    print "   | | |   || |  |_______|  / / || || || "
    print "   | | |  / / /( |_______/) |  / | || ||"
    print "  / / /  / /  | /________| /|  \ \ || ||"
    print " / / /  / /___\|________/ / /___\ \ \ \ \ "
    print "|  | | /_/    /________|  \      \_| \ \ \ "
    print "|  |_|__/ ___/________/\   \_     \__|_|  \ "
    print "|  /     /  /\________/ \    \_         \  |"
    print "| /     /  /\________/  |      \__       \ |      /\ "
    print "|/     /  /\________/   |         \___    \|_____/  \ "
    print "v     /  |\________|    |             \___/         |"
    print "     /   |\________|    |                        __/"
    print "     \    \________\     \                   ___/"
    print "   __/    /\_______/     /\_,          _____/"
    print " / ______/\uuuuu/ ______/   \________/"
    print " VVV     V      VVV    V "
    


    spell_menu.options.insert(-1, menu_class.Option(hero.spells[0].name, lambda: hero.spells[0].fire(hero, dragon)))
    spell_menu.options.insert(-1, menu_class.Option(hero.spells[1].name, lambda: hero.spells[1].fire(hero, dragon)))
    spell_menu.options.insert(-1, menu_class.Option(hero.spells[2].name, lambda: hero.spells[2].fire(hero, dragon)))

    item_menu.options.insert(-1, menu_class.Option(hero.inventory[0].name, lambda: hero.inventory[0].use(hero)))
    item_menu.options.insert(-1, menu_class.Option(hero.inventory[1].name, lambda: hero.inventory[1].use(hero)))
    item_menu.options.insert(-1, menu_class.Option(hero.inventory[2].name, lambda: hero.inventory[2].use(hero)))


    print '\nOkay, ' + hero.name + ", it's time to FIGHT!!\n"

    while hero.health > 0 and dragon.health > 0:
        hero.show_status()
        dragon.show_status()
        get_input(main_menu)
        rand_upgrade()

        if dragon.health <= 15 and dragon.mana >= 5 and random.randrange(1, 10) > 6:
            dragon.heal()
        elif random.randrange(1, 10) > 6 and dragon.mana >= 5:
            dragon.breath_fire(hero)
        else:
            dragon.attack(hero)

    if hero.health <= 0:
        print "You have DIED!"
    else:
        print "You have slain the mighty dragon!!!"
    play_again = raw_input("Want to play again? [Y/N]\n".upper())
    if play_again == "Y" or play_again == "y":
        subprocess.call(['python', 'dragon_game.py'])
    else:
        exit(0)

def rand_upgrade():
    if random.randrange(1, 100) > 65 and hero.special > 0:
        print "You discovered a powerful AXE!  I wonder what happened to the previous owner..."
        main_menu.options.append(menu_class.Option("Special Attack", lambda: hero.special_attack(dragon, main_menu)))

def get_input(menu):
    selection = raw_input(menu.print_menu())
    for i, option in enumerate(menu.options):
        if option.title == selection:
            if not option.execute():
                get_input(menu)
            return True
    print "You done messed up kid, try again!"
    get_input(menu)


start_game()

