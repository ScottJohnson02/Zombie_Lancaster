import inventory
import loot
import random


# generic scene
class Scene(object):
    def __init__(self):
        self.inventory_system = inventory.inventory

    def help(self):
        """Shows all possible commands in the game"""
        print("""COMMANDS: loot - allows you to loot a building and search for items
leave - don't loot an area and continue walking
inventory - allows you to equip items and consume health items
help - enters this screen""")
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
        print("""Welcome to Lancaster
TYPE Help to learn to play or type start to start your adventure you can also type
inventory to equip items before your adventure""")
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
