
class Scene(object):
    def help(self):
        print("ENTER HOW TO PLAY AN ADDED FEATURES HERE")

    def loot(self):
        pass

    def inventory(self):
        pass


class Start(Scene):
    def enter(self):
        print("Welcome to Lancaster")
        pass


class Apartment(Scene):
    def enter(self):
        pass


class Gym(Scene):
    def enter(self):
        pass


class Parked_Car(Scene):
    def enter(self):
        pass


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
        pass
