import random
import zombie_scenes as zombie

game_length = 3


class Map(object):
    def __init__(self):
        self.scenes = [zombie.Apartment(), zombie.Gym(), zombie.Parked_Car(),
                       zombie.Thaddeus_Stevens(), zombie.Central_Market(),
                       zombie.Fulton_Theater()]
        self.start = self.scenes[0]

    def create(self):
        random.shuffle(self.scenes)
        while len(self.scenes) > game_length:
            self.scenes.pop()
        self.scenes.insert(0, zombie.Start())
        self.scenes.append(zombie.Finish())
        self.current = self.scenes[0]

    def next(self):
        self.scenes.pop(0)


# game_map = Map()
# game_map.create()
# print(game_map.scenes[0])
# game_map.next()
# game_map.next()
# game_map.next()
# game_map.next()
