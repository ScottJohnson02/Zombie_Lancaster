import zombie_scenes as zombie


class falling(zombie.Scene):
    def death(self):
        print("You fell and died")


class eaten(zombie.Scene):
    def death(self):
        print("You got eaten and died")


class shot(zombie.Scene):
    def death(self):
        print("You got shot and died")


test = falling()
test.help()
