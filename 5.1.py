class Monster:
    def __init__(self, hitpoints, damage, range):
        self.hitpoints = hitpoints
        self.damage = damage
        self.range = range
    def charge(self):
        print(f"Damage done = {self.damage}")
class Goblin(Monster):
    def __init__(self, hitpoints, damage, country_of_origin):
        Monster.__init__(self,hitpoints,damage,range)
        self.country_of_origin = country_of_origin
        self.__gold = 0
    def charge(self):
        print(f"Goblin is coming for you. Damage = {self.damage}")

    def steal_gold(self, how_much_gold):
        self.__gold +=how_much_gold
    @property
    def gold(self):
        return self.__gold

class FriendlyGoblin(Goblin):
    def __init__(self, hitpoints, damage, range, country_of_origin, fuzziness_factor):
        Goblin.__init__(self,hitpoints,damage,range, country_of_origin)
        self.fuzzy = fuzziness_factor

        def charge(self):
            print(f"Here comes a huge fuzzy hug. How fuzzy? {self.fuzzy} fuzzy")

        def steal_gold(self, how_much_gold):
            print(f"")
