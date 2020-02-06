import player
import random
import time


class Zombie(object):
    """Creates a zombie with the atributes name , health, defense, and attack"""

    def create(self, name, health, defense, attack):
        self.hp = health
        self.defense = defense
        self.atk = attack
        self.name = name
# have to make a new zombie object each time


class CreateEncounter(object):

    def start(self, enemy):
        """Creates a combat exchange between player and a zombie"""
        # enemy has hp,def,atk,and name atributes
        self.player = player.character
        self.enemy = enemy

        def human_crit_calc(dmg, name, zombie_armor, zombie_health):
            # calculates damage done to zombie
            count = random.randint(1, 10)
            new_dmg = dmg - zombie_armor
            if new_dmg < 0:
                new_dmg = 0
            if count == 1:
                print(
                    f"!CRITICAL STRIKE!{self.player.name} attacks and deals {2 * new_dmg} damage!")
                zombie_health -= 2 * new_dmg
                return zombie_health

            else:
                print(f" {self.player.name} attacks and deals {new_dmg} damage!")
                zombie_health -= new_dmg
                return zombie_health

        def zombie_crit_calc(dmg, name, human_armor, human_health):
            # calculates damage done to player
            count = random.randint(1, 15)
            new_dmg = dmg - human_armor
            if new_dmg < 0:
                new_dmg = 0
            if count == 1:
                print(
                    f"!CRITICAL HIT!{enemy.name} attacks and deals {2 * new_dmg} damage!")
                human_health -= 2 * new_dmg
                return human_health
            elif count == 2:
                print(f"MISS! {enemy.name} attacks and deals 0 damage!")
                return human_health
            else:
                new_dmg = dmg - human_armor
                if dmg - human_armor < 0:
                    new_dmg = 0
                print(f" {name} attacks and deals {new_dmg}!")
                human_health -= new_dmg
                return human_health

        print(f"Enemy {self.enemy.name} wants to fight!")
        while self.player.hp >= 0 and enemy.hp >= 0:
            print(
                f'YOUR CURRENT HEALTH: {self.player.hp} ENEMY HEALTH: {self.enemy.hp}')
            self.enemy.hp = human_crit_calc(self.player.atk, self.player.name,
                                            self.enemy.defense, self.enemy.hp)
            if self.enemy.hp <= 0:
                print(f"{self.player.name} has killed {self.enemy.name}!")
                print(f'YOUR REMAINING HEALTH: {self.player.hp}')
                break

            time.sleep(1.5)

            self.player.hp = zombie_crit_calc(self.enemy.atk, self.enemy.name,
                                              self.player.defense, self.player.hp)
            if self.player.hp <= 0:
                print(f"{self.enemy.name} has killed you GAME OVER!")
                quit()
            time.sleep(1.5)


# bruh = CreateEncounter()
# zombie = possible_zombies.get('crawler')
# print(zombie.name)
# bruh.start(zombie)
# zombie = possible_zombies.get('crawler')
# print(zombie.hp)
