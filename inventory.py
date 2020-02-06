class Item(object):
    def __init__(self, name, attack, armor, health, rarity):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.health = health
        self.rarity = rarity
        # 7 common
        # 1 very rare


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        # add an item to your inventory
        self.items[item.name] = item

    def print_items(self):
        # print your items
        print("YOUR INVENTORY:")
        for item in self.items.values():
            # checks each item in the players inventory and prints a description
            print(f"{item.name}: provides ", end='')
            if item.attack > 0:
                print(f"{item.attack} attack when equiped")
            if item.armor > 0:
                print(f"{item.armor} armor when worn")
            if item.health > 0:
                print(f"{item.health} health when consumed/used")


inventory = Inventory()
# inventory.add_item(Item('Bandage', 0, 0, 2, 5))
# inventory.add_item(Item('Beanie', 0, 1, 0), 5)
# inventory.print_items()

possible_items = {
    'Bandage': Item('Bandage', 0, 0, 2, 4),
    'Beanie': Item('Beanie', 0, 1, 0, 4),
    'Timbs': Item('Beanie', 0, 1, 0, 3),
    'Flannel': Item('Flannel', 0, 1, 0, 4),
    'Pain-Away': Item('Pain-Away', 0, 0, 5, 2),
    'Baseball Bat': Item('Baseball Bat', 3, 0, 0, 5),
    'ShotGun': Item('ShotGun', 15, 0, 0, 2),
    'Pistol': Item('Pistol', 7, 0, 0, 3),
    'Sharp Pencil': Item('Sharp Pencil', 1, 0, 0, 1),
    'Barbed Bat': Item('Barbed Bat', 7, 0, 0, 3),
    'Riot Gear': Item('Riot Gear', 0, 10, 0, 1),
    'Chef Knife': Item('Chefs Knife', 5, 0, 0, 4),
    'Butchers Knife': Item('Butchers Knife', 7, 0, 0, 3),
    'Fedor Fighting Knife': Item('Fedor Fighting Knife', 10, 0, 0, 1),
    'Amish Axe': Item('Amish Axe', 9, 0, 0, 2),
    'Subway Sub': Item('Subway Sub', 0, 0, 2, 4),
    'Hacky Sack': Item('Hacky Sack', 1, 0, 0, 5),
}
