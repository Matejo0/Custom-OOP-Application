import random
import json
import datetime

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
        
class Game:
    def __init__(self):
        self.characters = []
        self.player = None
        self.opponent = None
        self.log_file = None

    def load_characters_from_config(self):
        with open("Custom-OOP-Application\config.json", "r") as file:
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
        
    def create_log_file(self):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.log_file = open(f"log.{current_date}.txt", "w")

    def write_to_log_file(self, message):
        self.log_file.write(message + "\n")

    def close_log_file(self):
        self.log_file.close()

    def play(self):
        self.load_characters_from_config()
        self.select_character()
        self.create_log_file()
        self.write_to_log_file(f"Rozpoczynasz walkę jako {self.player.name} przeciwko {self.opponent.name}!")

        while self.player.health > 0 and self.opponent.health > 0:
            print(f"\nTwoje zdrowie: {self.player.health}")
            print(f"Zdrowie przeciwnika: {self.opponent.health}")
            self.write_to_log_file(f"\nTwoje zdrowie: {self.player.health}")
            self.write_to_log_file(f"Zdrowie przeciwnika: {self.opponent.health}")

            choice = input("\nWybierz akcję:\n1. Atak\n2. Unik\nWybór: ")
            if choice == "1":
                if self.opponent.dodge()== False:
                    self.player.attack(self.opponent)
                    self.opponent.attack(self.player)
                else:
                    continue
            elif choice == "2":
                if self.player.dodge() == False:
                    print("Nie udany unik")
                    self.write_to_log_file(f"{self.player.name} nie unika ataku")
                    self.player.attack(self.opponent)
                    self.opponent.attack(self.player)
                else:
                    continue
                    
            else:
                self.write_to_log_file("Nieprawidłowy wybór, spróbuj ponownie.")
                print("Nieprawidłowy wybór, spróbuj ponownie.")

        if self.player.health > 0:
            print("Wygrałeś walkę!")
            self.write_to_log_file("Wygrałeś walkę!")
        else:
            print("Przegrałeś walkę!")
            self.write_to_log_file("Przegrałeś walkę!")

        self.close_log_file()

game = Game()
game.play()
