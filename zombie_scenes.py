import inventory
import loot
import random
from textwrap import dedent


# generic scene
class Scene(object):
    def __init__(self):
        self.inventory_system = inventory.inventory

    def help(self):
        """Shows all possible commands in the game"""
        print(dedent("""-----COMMANDS-----
        ---------------------------------------------------------------
        loot - allows you to loot a building and search for items
        leave - don't loot an area and continue walking
        inventory - allows you to equip items and consume health items
        help - enters this screen
        ---------------------------------------------------------------"""))
        return self.enter()

    def loot(self, risk):
        """Takes a number and is equivelent to 1/10 for 1 and 2/10 for 2 etc..."""
        # risk is a 1 out of 10 chance to get killed
        self.risk = random.randint(1, 10)
        if 1 <= self.risk <= risk:
            return "death"

        else:
            self.loot = loot.Loot()
            self.loot.find(risk)

    def inventory(self):
        """inventory system for beginning of scene"""
        self.inventory_system.equip()
        return self.enter()

    def inventory2(self):
        """inventory system for end of scene if looting is successful"""
        self.inventory_system.equip()
        return 'next'

    def loot_Success(self):
        """Asks the user for input after the scene to see if they want to do anything"""
        print("Do you want to do anything before you go to the next location? type continue to continue")
        choice = input("> ")
        if choice.upper() == "HELP":
            return self.help()
        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
        elif choice.upper() == "CONTINUE":
            # continues with the game
            print("You decided to head on the road")
        elif choice.upper() == "INVENTORY":
            return self.inventory2()
        else:
            print("INVALID MOVE")
            return self.loot_Success()


class Start(Scene):
    def enter(self):
        print(dedent("""
        ----------------------------------------------------------------------------

        The year is 20XX and due to an unknown pathogen outbreak civilization as
        we know it has been reduced to rubble. Larger cities fell first due to the
        population density. You are currently in your old apartment but the Z's are
        pounding on your rear door and will break through any moment. You decide
        to gather what you can and you bolt out the front door and head on the
        streets. You know that it is safer on the outskirts of the city but you
        have to go through the thick of it if you want to escape to the other
        side and get to a local farm and live out the rest of days.

        ----------------------------------------------------------------------------

        HOW TO PLAY: You will walk around on the streets looking for places to loot
        and you will encounter zombies that you will have to fight in order to keep
        progressing. Once you get to a new location you will have the option to
        loot the area or leave. There is also a risk associated with each location
        1 is 10% chance and 5 is 50% chance to fail. However the higher the risk
        the higher chance you have to find powerful loot. You can also press type
        "inventory" at anytime to view your current inventory and equip items.
        You currently have a few items in your inventory when you are done equipping
        gear type "start" to begin your adventure through Lancaster City"""))
        choice = input("> ")
        if choice.upper() == "HELP":
            return self.help()
        elif choice.upper() == "START":
            print("")
        elif choice.upper() == "INVENTORY":
            return self.inventory()
        else:
            print("INVALID MOVE")
            return self.enter()


class Apartment(Scene):
    def enter(self):
        print("You come across an appartment with an open door what do you do?")
        choice = input("> ")
        if choice.upper() == "HELP":
            return self.help()
        elif choice.upper() == "LOOT":
            print("You loot the apartment")
            self.loot(1)
            return self.loot_Success()

        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
        elif choice.upper() == "LEAVE":
            print("You decided not too loot the apartment")
        elif choice.upper() == "INVENTORY":
            return self.inventory()
        else:
            print("INVALID MOVE")
            return self.enter()


class Gym(Scene):
    def enter(self):
        print("You come across the old GYM with an open door what do you do? Risk: 3/10")
        choice = input("> ")
        if choice.upper() == "HELP":
            return self.help()
        elif choice.upper() == "LOOT":
            print("You loot the GYM")
            self.loot(3)
            return self.loot_Success()
        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
        elif choice.upper() == "LEAVE":
            print("You decided not too loot the GYM")
        elif choice.upper() == "INVENTORY":
            return self.inventory()
        else:
            print("INVALID MOVE")
            return self.enter()


class Parked_Car(Scene):
    def enter(self):
        print("You come across a parked car with an open door what do you do? Risk: 2/10")
        choice = input("> ")
        if choice.upper() == "HELP":
            return self.help()
        elif choice.upper() == "LOOT":
            print("You loot the car")
            self.loot(2)
            return self.loot_Success()
        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
        elif choice.upper() == "LEAVE":
            print("You decided not too loot the car")
        elif choice.upper() == "INVENTORY":
            return self.inventory()
        else:
            print("INVALID MOVE")
            return self.enter()


class Thaddeus_Stevens(Scene):
    def enter(self):
        print("You come to the Thaddeus Stevens main campus. Do you loot the campus? Risk: 5/10!")
        choice = input("> ")
        if choice.upper() == "HELP":
            return self.help()
        elif choice.upper() == "LOOT":
            print("You loot the campus")
            self.loot(5)
            return self.loot_Success()
        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
        elif choice.upper() == "LEAVE":
            print("You decided not too loot the campus")
        elif choice.upper() == "INVENTORY":
            return self.inventory()
        else:
            print("INVALID MOVE")
            return self.enter()


class Central_Market(Scene):
    def enter(self):
        print("""You come across the Central Market. There is a hole in the
wall where you could squeeze through. Do you want to loot it? Risk: 2/10""")
        choice = input("> ")
        if choice.upper() == "HELP":
            return self.help()
        elif choice.upper() == "LOOT":
            print("You loot the market")
            self.loot(2)
            return self.loot_Success()
        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
        elif choice.upper() == "LEAVE":
            print("You decided not too loot the market")
        elif choice.upper() == "INVENTORY":
            return self.inventory()
        else:
            print("INVALID MOVE")
            return self.enter()


class Fulton_Theater(Scene):
    def enter(self):
        print("You come across the Fulton Theater. There is a window open. Do you loot? Risk: 3/10")
        choice = input("> ")
        if choice.upper() == "HELP":
            return self.help()
        elif choice.upper() == "LOOT":
            print("You loot the building")
            self.loot(3)
            return self.loot_Success()
        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
        elif choice.upper() == "LEAVE":
            print("You decided not too loot the theater")
        elif choice.upper() == "INVENTORY":
            return self.inventory()
        else:
            print("INVALID MOVE")
            return self.enter()


class Finish(Scene):
    def enter(self):
        print("You win and go to a local farm and live out your last of days")
