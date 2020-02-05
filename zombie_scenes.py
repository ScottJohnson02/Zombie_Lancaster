import inventory


class Scene(object):
    def help(self):
        print("ENTER HOW TO PLAY AN ADDED FEATURES HERE")

    def loot(self):
        self.items = inventory.possible_items
        print(self.items)

    def inventory(self):
        pass


class Start(Scene):
    def enter(self):
        print("Welcome to Lancaster")


class Apartment(Scene):
    def enter(self):
        print("You are in an apartment what do you do")
        choice = input("> ")
        if choice.upper() == "HELP":
            print('This will show hints and continue the scene')
            return self.enter()
        elif choice.upper() == "LOOT":
            print("You loot the apartment")
        elif choice.upper() == "DIE":
            print("Wrong move")
            return "death"
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
