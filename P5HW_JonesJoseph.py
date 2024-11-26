#Joseph Jones
#11/26/2024
#P5HW
#Using AI to make a pyhton code game

import random

def create_character():
    """
    Prompts the user to input character attributes and returns them as a dictionary.
    """
    name = input("Enter the character's name: ")
    try:
        health = int(input("Enter the character's health (integer): "))
        attack_points = int(input("Enter the character's attack points (integer): "))
    except ValueError:
        print("Invalid input. Health and attack points should be integers.")
        return None

    return {"name": name, "health": health, "attack_points": attack_points}

def display_characters(characters):
    """
    Displays the attributes of each character in a list of character dictionaries.
    """
    if not characters:
        print("No characters to display.")
        return

    for index, character in enumerate(characters, start=1):
        print(f"Character {index}:")
        for key, value in character.items():
            print(f"  {key.capitalize()}: {value}")
        print()

def battle(attacker, defender):
    """
    Simulates a battle scenario where the attacker damages the defender.

    Args:
        attacker (dict): The attacking character.
        defender (dict): The defending character.

    Returns:
        dict: The updated defender after taking damage.
    """
    multiplier = random.uniform(0.8, 1.2)
    damage = int(attacker["attack_points"] * multiplier)

    print(f"{attacker['name']} attacks {defender['name']}!")
    print(f"Base attack points: {attacker['attack_points']}")
    print(f"Multiplier applied: {multiplier:.2f}")
    print(f"Damage dealt: {damage}")

    defender["health"] -= damage
    if defender["health"] < 0:
        defender["health"] = 0

    print(f"{defender['name']}'s health is now {defender['health']}\n")
    return defender

def simulate_battle(attacker, defender):
    """
    Simulates a full battle between two characters, allowing the user to view each move or skip to the result.

    Args:
        attacker (dict): The first attacking character.
        defender (dict): The first defending character.
    """
    while attacker["health"] > 0 and defender["health"] > 0:
        defender = battle(attacker, defender)
        if defender["health"] == 0:
            print(f"{defender['name']} has been defeated! {attacker['name']} wins!\n")
            return

        # Ask the user if they want to see the next move
        next_move = input("Do you want to see the next move? (yes/no): ").strip().lower()
        if next_move != "yes":
            break

        # Switch roles: defender becomes attacker and vice versa
        attacker, defender = defender, attacker

    # Determine and display the winner
    if attacker["health"] > 0:
        print(f"{attacker['name']} wins the battle!")
    else:
        print(f"{defender['name']} wins the battle!")

def main():
    """
    Main function to manage the game menu.
    """
    characters = []

    while True:
        print("\nMenu:")
        print("1. Create a character")
        print("2. Display characters")
        print("3. Simulate a battle")
        print("4. Exit")
        print()
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            character = create_character()
            if character:
                characters.append(character)
                print(f"Character '{character['name']}' created successfully!")
        
        elif choice == "2":
            display_characters(characters)
        
        elif choice == "3":
            if len(characters) < 2:
                print("You need at least two characters to simulate a battle.")
                continue
            
            display_characters(characters)
            try:
                attacker_index = int(input("Choose the attacker (1-based index): ")) - 1
                defender_index = int(input("Choose the defender (1-based index): ")) - 1
                
                if attacker_index == defender_index:
                    print("Attacker and defender cannot be the same character.")
                    continue
                
                attacker = characters[attacker_index]
                defender = characters[defender_index]
                simulate_battle(attacker, defender)
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")
        
        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Run the game
if __name__ == "__main__":
    main()
