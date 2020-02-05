import zombie_scenes as zombie


class Fell(zombie.Scene):
    def death(self):
        print("You fell and died")


class Eaten(zombie.Scene):
    def death(self):
        print("You got eaten and died")


class Shot(zombie.Scene):
    def death(self):
        print("You got shot and died")


deaths = {
    'shot': Shot(),
    'eaten': Eaten(),
    'fell': Fell()
}
