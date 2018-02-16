
# dynamically create cells for a dungeon

class Cell:
    def __init__(self):
        pass
    pass

class Dungeon:
    def __init__(self):
        pass
    pass

class DungeonFactory:
    def __init__(self, bosses, monsters):
        """
        args:
            bosses      list of bosses in this cell

            monsters    dictionary keyed by tiers which map to list of monsters
                            ex:
                            monsters = {
                              0:[easiest monsters],
                              1:[monsters harder than 0]
                              2:[monsters harder than 1]
                              3:[monsters harder than 2]
                              ...
                              n:[nth tier monsters]
                            }

        """
        self.bosses = bosses
        self.monsters = monsters
        pass

    def generate_dungeon(difficulty_distribution):
        pass

    pass

