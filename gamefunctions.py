import random, json

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, opponent):
        damage = random.randint(1, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} zadaje {damage} obrażeń {opponent.name}!")

    def dodge(self):
        if random.randint(1,10) < 3:
            print(f"{self.name} unika ataku przeciwnika!")
            return True
        else:
            return False
