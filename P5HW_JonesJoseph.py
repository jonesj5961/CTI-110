# Joseph Jones
# 12/3/2024
# P5HW
# Using the help of Ai create a python code game

import random

class Champion:
    def __init__(self, name, gender, champion_class, weapon, special_attribute, element=None):
        self.name = name
        self.gender = gender
        self.champion_class = champion_class
        self.weapon = weapon
        self.special_attribute = special_attribute
        self.element = element
        self.health = 100  # Hardcoded health
        self.attack_points = random.randint(10, 20)  # Random initial attack points
        self.luck = random.randint(1, 10)
        self.level = 1
        self.experience = 0
        self.gold = 0
        self.inventory = []
        self.status_effects = []
        self.battle_history = {"wins": 0, "losses": 0}

    def level_up(self):
        self.level += 1
        self.attack_points += random.randint(2, 5)
        self.luck += 1
        self.health = 100  # Restore health on level up
        print(f"{self.name} has leveled up! Now at Level {self.level}.")

    def add_experience(self, xp):
        self.experience += xp
        print(f"{self.name} gained {xp} XP!")
        if self.experience >= self.level * 100:
            self.level_up()
            self.experience = 0

    def add_gold(self, amount):
        self.gold += amount
        print(f"{self.name} earned {amount} gold! Total gold: {self.gold}.")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{self.name} added {item} to their inventory.")

    def show_stats(self):
        print(f"\nChampion: {self.name}")
        print(f"  Gender: {self.gender}")
        print(f"  Class: {self.champion_class}")
        print(f"  Weapon: {self.weapon}")
        print(f"  Special Attribute: {self.special_attribute}")
        if self.weapon == "Staff" and self.element:
            print(f"  Element: {self.element}")
        print(f"  Level: {self.level}")
        print(f"  Health: {self.health}")
        print(f"  Attack Points: {self.attack_points}")
        print(f"  Luck: {self.luck}")
        print(f"  Experience: {self.experience}")
        print(f"  Gold: {self.gold}")
        print(f"  Status Effects: {', '.join(self.status_effects) if self.status_effects else 'None'}")
        print(f"  Battle History: {self.battle_history['wins']} Wins, {self.battle_history['losses']} Losses")
        print(f"  Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")

def create_champion():
    print("\nWould you like to create your champion or have one generated for you?")
    print("1. Create your own champion")
    print("2. Generate a random champion")
    choice = input("Enter your choice (1-2): ").strip()

    if choice == "1":
        name = input("Enter the champion's name: ")
        gender = input("Enter the champion's gender (male/female): ").strip().lower()
        while gender not in ["male", "female"]:
            gender = input("Invalid gender. Please enter 'male' or 'female': ").strip().lower()

        print("Choose a class:")
        classes = {
            "1": "Warrior",
            "2": "Archer",
            "3": "Mage",
            "4": "Rogue"
        }
        for key, value in classes.items():
            print(f"{key}. {value}")
        class_choice = input("Enter your choice (1-4): ").strip()
        champion_class = classes.get(class_choice, "Warrior")

        print("Choose a weapon:")
        weapons = {
            "1": ("Sword", "Critical Hit"),
            "2": ("Bow", "Multi-Strike"),
            "3": ("Staff", "Elemental Magic"),
            "4": ("Daggers", "Bleed")
        }
        for key, (weapon, special) in weapons.items():
            print(f"{key}. {weapon} (Special Attribute: {special})")
        weapon_choice = input("Enter your choice (1-4): ").strip()
        weapon, special_attribute = weapons.get(weapon_choice, ("Sword", "Critical Hit"))

        element = None
        if weapon == "Staff":
            print("Choose an element for your Staff:")
            elements = {
                "1": "Earth",
                "2": "Fire",
                "3": "Air",
                "4": "Ice"
            }
            for key, value in elements.items():
                print(f"{key}. {value}")
            element_choice = input("Enter your choice (1-4): ").strip()
            element = elements.get(element_choice, "None")

        return Champion(name, gender, champion_class, weapon, special_attribute, element)

    elif choice == "2":
        return generate_random_champion()

def generate_random_champion():
    name = f"AI_Champion_{random.randint(1000, 9999)}"
    gender = random.choice(["male", "female"])
    champion_class = random.choice(["Warrior", "Archer", "Mage", "Rogue"])
    weapon, special_attribute = random.choice(
        [("Sword", "Critical Hit"), ("Bow", "Multi-Strike"), ("Staff", "Elemental Magic"), ("Daggers", "Bleed")]
    )
    element = None
    if weapon == "Staff":
        element = random.choice(["Earth", "Fire", "Air", "Ice"])

    return Champion(name, gender, champion_class, weapon, special_attribute, element)

def generate_ai_champion(difficulty):
    # AI champion attributes based on difficulty
    name = f"AI_Champion_{random.randint(1000, 9999)}"
    gender = random.choice(["male", "female"])
    champion_class = random.choice(["Warrior", "Archer", "Mage", "Rogue"])
    weapon, special_attribute = random.choice(
        [("Sword", "Critical Hit"), ("Bow", "Multi-Strike"), ("Staff", "Elemental Magic"), ("Daggers", "Bleed")]
    )
    element = None
    if weapon == "Staff":
        element = random.choice(["Earth", "Fire", "Air", "Ice"])

    ai_champion = Champion(name, gender, champion_class, weapon, special_attribute, element)

    # Adjust stats based on difficulty
    if difficulty == "easy":
        ai_champion.health = random.randint(50, 70)
        ai_champion.attack_points = random.randint(5, 10)
    elif difficulty == "moderate":
        ai_champion.health = random.randint(70, 100)
        ai_champion.attack_points = random.randint(10, 15)
    elif difficulty == "hard":
        ai_champion.health = random.randint(100, 120)
        ai_champion.attack_points = random.randint(15, 20)
    elif difficulty == "expert":
        ai_champion.health = random.randint(120, 150)
        ai_champion.attack_points = random.randint(20, 25)

    return ai_champion

def battle(attacker, defender):
    print(f"\nBattle starts between {attacker.name} and {defender.name}!")
    while attacker.health > 0 and defender.health > 0:
        damage = attacker.attack_points + random.randint(1, 5)
        defender.health -= damage
        print(f"{attacker.name} attacks {defender.name} for {damage} damage!")
        print(f"{defender.name}'s health: {defender.health}")

        if defender.health > 0:
            damage = defender.attack_points + random.randint(1, 5)
            attacker.health -= damage
            print(f"{defender.name} attacks {attacker.name} for {damage} damage!")
            print(f"{attacker.name}'s health: {attacker.health}")

        if attacker.health <= 0 or defender.health <= 0:
            break

    if attacker.health > 0:
        print(f"{attacker.name} wins the battle!")
        attacker.battle_history["wins"] += 1
        defender.battle_history["losses"] += 1
        return attacker
    else:
        print(f"{defender.name} wins the battle!")
        defender.battle_history["wins"] += 1
        attacker.battle_history["losses"] += 1
        return defender

def tournament(player_champion):
    print("\nTournament Mode: Choose tournament size:")
    print("1. 8 Champions")
    print("2. 10 Champions")
    print("3. 20 Champions")
    tournament_size = input("Enter your choice (1-3): ").strip()

    tournament_sizes = {
        "1": 8,
        "2": 10,
        "3": 20
    }

    num_champions = tournament_sizes.get(tournament_size, 8)
    tournament_champions = [player_champion]

    # Generate AI champions
    for _ in range(num_champions - 1):
        difficulty = random.choice(["easy", "moderate", "hard", "expert"])
        ai_champion = generate_ai_champion(difficulty)
        tournament_champions.append(ai_champion)

    random.shuffle(tournament_champions)  # Shuffle to randomize the tournament bracket
    round_number = 1
    while len(tournament_champions) > 1:
        print(f"\nRound {round_number}")
        round_winners = []
        for i in range(0, len(tournament_champions), 2):
            print(f"Match: {tournament_champions[i].name} vs {tournament_champions[i+1].name}")
            winner = battle(tournament_champions[i], tournament_champions[i+1])
            round_winners.append(winner)
        tournament_champions = round_winners
        round_number += 1

    winner = tournament_champions[0]
    print(f"\nThe winner of the tournament is {winner.name}!")
    print(f"You lasted {round_number - 1} rounds.")

def story_mode():
    print("\nStory Mode: Embark on your adventure!")
    player_champion = create_champion()
    print(f"Your champion: {player_champion.name}")

    # Loop through story chapters
    chapter = 1
    while True:
        print(f"\n--- Chapter {chapter} ---")
        print(f"{player_champion.name}, you are about to face an enemy!")
        ai_champion = generate_ai_champion(random.choice(["easy", "moderate", "hard", "expert"]))

        print(f"Your opponent: {ai_champion.name}")
        winner = battle(player_champion, ai_champion)

        if winner == player_champion:
            print(f"{player_champion.name} won the battle!")
            player_champion.add_experience(50)
            player_champion.add_gold(100)

            item = random.choice(["Health Potion", "Strength Potion", "Speed Potion", "Shield"])
            player_champion.add_to_inventory(item)
        else:
            print(f"{player_champion.name} lost the battle.")
            choice = input("Do you want to restart? (yes/no): ").strip().lower()
            if choice == "yes":
                chapter = 1
                player_champion.health = 100  # Reset health
                player_champion.experience = 0  # Reset experience
                player_champion.inventory = []  # Clear inventory
            else:
                break

        chapter += 1

    print("Returning to the main menu.")

def main():
    champions = []

    while True:
        print("\nCHAMPIONS OF THE REALM")  # Title in all caps
        print("\nMain Menu:")
        print("1. Create Champion")
        print("2. Display Champions")
        print("3. Battle")
        print("4. Tournament Mode")
        print("5. Story Mode")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            champions.append(create_champion())
        elif choice == "2":
            if not champions:
                print("No champions created yet.")
            else:
                for champion in champions:
                    champion.show_stats()
        elif choice == "3":
            if len(champions) < 2:
                print("Not enough champions to start a battle. Create more champions.")
            else:
                print("Choose difficulty level for AI:")
                print("1. Easy")
                print("2. Moderate")
                print("3. Hard")
                print("4. Expert")
                difficulty_choice = input("Enter your choice (1-4): ").strip()
                difficulty_levels = {
                    "1": "easy",
                    "2": "moderate",
                    "3": "hard",
                    "4": "expert"
                }
                difficulty = difficulty_levels.get(difficulty_choice, "easy")
                ai_champion = generate_ai_champion(difficulty)
                print(f"Generated AI Champion: {ai_champion.name}")
                battle(champions[0], ai_champion)
        elif choice == "4":
            if not champions:
                print("No champions created yet.")
            else:
                tournament(champions[0])
        elif choice == "5":
            story_mode()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
