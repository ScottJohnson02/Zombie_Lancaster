import inventory
import loot
import random
# need dedent


class Scene(object):
    def help(self):
        print("""COMMANDS: loot - allows you to loot a building and search for items
leave - don't loot an area and continue walking
inventory - allows you to equip items and consume health items
help - enters this screen""")
        return self.enter()

    def loot(self, risk):
        # risk is a 1 out of 10 chance to get killed
        self.risk = random.randint(1, 10)
        if 1 <= self.risk <= risk:
            return "death"

        else:
            self.loot = loot.Loot()
            self.loot.find(risk)

    def inventory(self):
        self.inventory = inventory.inventory
        self.inventory.print_items()


# bruh = Scene()
# bruh.loot(6)


class Start(Scene):
    def enter(self):
        print("""Welcome to Lancaster
TYPE Help to learn to play or type start to start your adventure""")
        choice = input("> ")
        if choice.upper() == "HELP":
            return self.help()
        elif choice.upper() == "START":
            print("")
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
            return self.loot(1)
        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
        elif choice.upper() == "LEAVE":
            print("You decided not too loot the apartment")
        else:
            print("INVALID MOVE")
            return self.enter()


class Gym(Scene):
    def enter(self):
        print('gym')


class Parked_Car(Scene):
    def enter(self):
        print('car')


class Thaddeus_Stevens(Scene):
    def enter(self):
        pass


class Central_Market(Scene):
    def enter(self):
        pass


class Fulton_Theater(Scene):
    def enter(self):
        pass


class Finish(Scene):
    def enter(self):
        print("You win")
