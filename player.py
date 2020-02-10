class Player(object):
    """Creates a new player with name, and friend's name"""

    def __init__(self, name, friend):
        self.hp = 25
        self.name = name
        self.friend = friend
        self.atk = 3
        self.defense = 0


character = Player('Player', 'bruh')
