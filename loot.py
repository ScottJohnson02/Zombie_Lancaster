import inventory
import random


class Loot(object):
    def __init__(self):
        # adds a possible item to a list and takes the item rarity to determine how many of that item is put in the list
        self.loot = []
        self.items = inventory.possible_items
        count = 0
        for item in self.items.values():
            while item.rarity > count:
                count += 1
                self.loot.append(item)
            count = 0

    def find(self, number):
        # decides what loot you get depending on your number
        self.number = random.randint(1, number)
        self.inventory = inventory.inventory
        self.found_loot = []
        counter = 0
        if self.number == 0:
            print('You found no loot :(')
        while counter < self.number:
            random.shuffle(self.loot)
            item = self.loot[0]
            self.found_loot.append(item)
            self.loot.pop(0)
            print(f"You found a(n) {item.name} Rarity: ", end='')
            if item.rarity == 1:
                print("*" * 5)
            if item.rarity == 2 or item.rarity == 3:
                print("*" * 4)
            if item.rarity == 4:
                print("*" * 3)
            if item.rarity == 5:
                print("*" * 2)
            if item.rarity >= 6:
                print("*" * 1)
            if item.attack > 0:
                print(f"Provides {item.attack} attack when selected")
            if item.armor > 0:
                print(f"Provides {item.armor} armor when selected")
            if item.health > 0:
                print(f"Provides {item.health} health when selected")
            self.inventory.add_item(item)
            counter += 1


# bruh = Loot()
# bruh.find(3)
