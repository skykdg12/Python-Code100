class Wizard:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    def attack(self):
        print("파이어볼")
X = Wizard(545, 210, 10,)
print(X.health, X.mana, X.armor)
X.attack()