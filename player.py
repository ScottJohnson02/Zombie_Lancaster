class Player(object):
    def __init__(self, name, friend):
        self.hp = 20
        self.name = name
        self.friend = friend
        self.atk = 3
        self.defense = 1


character = Player('You', 'bruh')
