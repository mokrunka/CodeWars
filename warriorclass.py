class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def strike(self, enemy, swings):
        # health cannot go below zero
        enemy.health = max([0, enemy.health - (swings * 10)])

name = 'hattori hanzo'
ninja = Warrior(name)

name1 = 'stephan'
ninja1 = Warrior(name1)

print(ninja.name)
print(ninja1.name)

print(ninja1.strike(ninja, 3))
print(ninja.health)
print(ninja1.health)