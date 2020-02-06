import death_scenes
import zombie_map
import zombie_scenes
import random


class Game(object):
    def __init__(self, game_map, gameover):
        self.map = game_map
        self.gameover = gameover

    def play(self):
        index = 0
        self.map.create()
        print(self.map.scenes[index])
        while len(self.map.scenes) > 1:
            current = self.map.scenes[0].enter()
            if current == "death":
                print('You are die')
                break
            elif current == "help":
                pass
            elif current == "loot":
                pass
            else:
                self.map.next()


deaths = death_scenes.deaths
zombie_map = zombie_map.Map()
zombie_lancater = Game(zombie_map, deaths)
zombie_lancater.play()
