class Player:

    def __init__(self, name, level):

        self.name = name
        self.level = level

        pass

player = Player('Knight', 10)

print(player.level)

player.level = 11

print(player.level)