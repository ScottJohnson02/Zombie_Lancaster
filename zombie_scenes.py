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
        print("You come across the old GYM with an open door what do you do? Risk: 3/10")
        choice = input("> ")
        if choice.upper() == "HELP":
            return self.help()
        elif choice.upper() == "LOOT":
            print("You loot the GYM")
            return self.loot(3)
        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
        elif choice.upper() == "LEAVE":
            print("You decided not too loot the GYM")
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
            return self.loot(2)
        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
        elif choice.upper() == "LEAVE":
            print("You decided not too loot the car")
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
            return self.loot(5)
        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
        elif choice.upper() == "LEAVE":
            print("You decided not too loot the campus")
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
            return self.loot(2)
        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
        elif choice.upper() == "LEAVE":
            print("You decided not too loot the market")
        else:
            print("INVALID MOVE")
            return self.enter()


class Fulton_Theater(Scene):
    def enter(self):
        print("You come across the Fulton Theater. There is a window open. Do you enter? Risk: 3/10")
        choice = input("> ")
        if choice.upper() == "HELP":
            return self.help()
        elif choice.upper() == "LOOT":
            print("You loot the building")
            return self.loot(3)
        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
        elif choice.upper() == "LEAVE":
            print("You decided not too loot the theater")
        else:
            print("INVALID MOVE")
            return self.enter()


class Finish(Scene):
    def enter(self):
        print("You win and go to a local farm and live out your last of days")
