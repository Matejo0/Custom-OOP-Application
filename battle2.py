import random
import json

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
        if random.random() < 0.5:
            print(f"{self.name} unika ataku przeciwnika!")
            return True
        else:
            return False

class Game:
    def __init__(self):
        self.characters = []
        self.player = None
        self.opponent = None

    def load_characters_from_config(self):
        with open("config.json", "r") as file:
            data = json.load(file)
            self.characters = [
                Character(character["name"], character["health"], character["attack_power"])
                for character in data["characters"]
            ]

    def select_character(self):
        print("Wybierz postać:")
        for i, character in enumerate(self.characters):
            print(f"{i+1}. {character.name}")

        choice = input("Wybierz numer postaci: ")
        index = int(choice) - 1
        self.player = self.characters[index]

        remaining_characters = self.characters[:index] + self.characters[index+1:]
        self.opponent = random.choice(remaining_characters)

    def play(self):
        self.load_characters_from_config()
        self.select_character()
        print(f"Rozpoczynasz walkę jako {self.player.name} przeciwko {self.opponent.name}!")

        while self.player.health > 0 and self.opponent.health > 0:
            print(f"\nTwoje zdrowie: {self.player.health}")
            print(f"Zdrowie przeciwnika: {self.opponent.health}")

            choice = input("\nWybierz akcję:\n1. Atak\n2. Unik\nWybór: ")
            if choice == "1":
                if self.opponent.dodge() == False:
                    self.player.attack(self.opponent)
                    self.opponent.attack(self.player)

            elif choice == "2":
                if self.opponent.dodge():
                    continue
                else:
                    print("Przeciwnik nie unika ataku!")
                    self.opponent.attack(self.player)
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")

        if self.player.health > 0:
            print("Wygrałeś walkę!")
        else:
            print("Przegrałeś walkę!")

game = Game()
game.play()