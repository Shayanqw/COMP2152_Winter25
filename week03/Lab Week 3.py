import random

# Define Variables
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

diceOptions = list(range(1, 7))  # 1 to 6
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Display available weapons
print("Available Weapons:")
for index, weapon in enumerate(weapons, 1):
    print(f"{index}. {weapon}")


def get_combat_strength(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 6:
                return value
            else:
                print("Input must be an integer between 1-6")
        except ValueError:
            print("Input must be an integer between 1-6")


# Get combat strengths
combatStrength = get_combat_strength("\n Enter your combat Strength (1-6): ")
mCombatStrength = get_combat_strength("\n Enter the monster's combat Strength (1-6): ")

# Weapons list
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Simulate 10 rounds of battle (using step 2, range from 1 to 20)
for round_num in range(1, 21, 2):  # Simulating rounds 1, 3, 5, ..., 19
    hero_dice_roll = random.choice(diceOptions)
    monster_dice_roll = random.choice(diceOptions)

    combatStrength += hero_dice_roll
    mCombatStrength += monster_dice_roll

    hero_weapon = weapons[hero_dice_roll - 1]
    monster_weapon = weapons[monster_dice_roll - 1]

    print(f"Round {round_num}: Hero rolled {hero_dice_roll}, Monster rolled {monster_dice_roll}.")
    print(f"Hero selected: {hero_weapon}, Monster selected: {monster_weapon}.")
    print(f"Hero Total Strength: {combatStrength}, Monster Total Strength: {mCombatStrength}.")

    if combatStrength > mCombatStrength:
        print("Hero wins the round!\n")
    elif mCombatStrength > combatStrength:
        print("Monster wins the round!\n")
    else:
        print("It's a draw!\n")

    if round_num == 11:  # Battle Truce after round 11
        print("Battle Truce declared in Round 11. Game Over!")
        break
