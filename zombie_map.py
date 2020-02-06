import random
import zombie_scenes
import zombie_encounters

game_length = 3


class Map(object):
    def __init__(self):
        self.scenes = [zombie_scenes.Apartment(), zombie_scenes.Gym(),
                       zombie_scenes.Parked_Car(),
                       zombie_scenes.Thaddeus_Stevens(), zombie_scenes.Central_Market(),
                       zombie_scenes.Fulton_Theater()]
        self.start = self.scenes[0]
        self.zombie = zombie_encounters.Zombie()

    def create(self):
        random.shuffle(self.scenes)
        while len(self.scenes) > game_length:
            self.scenes.pop()
        self.scenes.insert(0, zombie_scenes.Start())
        self.scenes.append(zombie_scenes.Finish())
        self.current = self.scenes[0]

    def next(self):
        encounter_number = random.randint(1, 3)
        counter = 0
        while counter <= encounter_number:
            zombie_number = random.randint(1, 6)
            if zombie_number == 1 or zombie_number == 2:
                self.zombie.create("Crawler", 10, 0, 2)
            if zombie_number == 6:
                self.zombie.create("Police Zombie", 20, 2, 3)
            if zombie_number == 3 or zombie_number == 4:
                self.zombie.create("Walker", 15, 1, 2)
            if zombie_number == 5:
                self.zombie.create("Bloater", 30, 1, 3)
            zombie_encounters.CreateEncounter().start(self.zombie)
            counter += 1
        self.scenes.pop(0)


# game_map = Map()
# game_map.create()
# print(game_map.scenes[0])
# game_map.next()
# game_map.next()
# game_map.next()
# game_map.next()
