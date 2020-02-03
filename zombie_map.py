import random
import zombie_scenes as zombie

game_length = 3


class Map(object):
    def __init__(self):
        self.scenes = [zombie.Apartment(), zombie.Gym(), zombie.Parked_Car()]

    def create(self):
        random.shuffle(self.scenes)
        while len(self.scenes) > game_length:
            self.scenes.pop()
        self.scenes.insert(0, zombie.Start())
        self.scenes.append(zombie.Finish())
        print(self.scenes)


game_map = Map()
game_map.create()
