import random

# Define Variables
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

# Dice options as a list
diceOptions = list(range(1, 7))  # [1, 2, 3, 4, 5, 6]

# Display available weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
print("Available Weapons:")
for index, weapon in enumerate(weapons, 1):
    print(f"{index}. {weapon}")

# Player input validation for combat strength
while True:
    try:
        combatStrength = int(input("Enter your combat Strength: (Number between 1-6) "))
        if 1 <= combatStrength <= 6:
            break
        else:
            print("Input must be an integer between 1 and 6")
    except ValueError:
        print("Input must be an integer between 1 and 6")

# Monster input validation for combat strength
while True:
    try:
        mCombatStrength = int(input("Enter the monster's combat Strength: "))
        if 1 <= mCombatStrength <= 6:
            break
        else:
            print("Input must be an integer between 1 and 6")
    except ValueError:
        print("Input must be an integer between 1 and 6")

# Roll the dice for health points for the hero
input("Roll the dice for your health points (Press enter) ")
healthPoints = random.choice(diceOptions)
print("You rolled " + str(healthPoints) + " health points")

# Roll the dice for the monster's health points
input("Roll the dice for the monster's health points (Press enter) ")
mHealthPoints = random.choice(diceOptions)
print("You rolled " + str(mHealthPoints) + " health points for the monster")

# Roll the dice to check if the hero finds a healing potion
input("Roll the dice to see if you find a healing potion (Press enter) ")
healingPotion = random.choice([0, 1])
print("Have you found a healing potion?: " + str(bool(healingPotion)))

# Roll the dice (1-6) to choose which weapon the hero must use
weaponRoll = random.choice(range(6))  # roll from 0 to 5 (index for weapons)

# Add the weapon roll to the hero's combat strength
combatStrength += weaponRoll

# Display the name of the hero's weapon
print("The name of the hero's weapon is: " + weapons[weaponRoll])

# Print message based on the weapon roll
if weaponRoll <= 2:
    print("You rolled a weak weapon, friend")
elif weaponRoll <= 4:
    print("Your weapon is meh")
else:
    print("Nice weapon, friend!")

# If the weapon rolled is not a Fist, print a thank you message
if weapons[weaponRoll] != "Fist":
    print("Thank goodness you didn't roll the Fist...")

# Analyze the roll (comparison operations)
input("Analyze the roll (Press enter)")
print("--- You are matched in strength: " + str(combatStrength == mCombatStrength))
print("--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))
print("--- Remember to take a healing potion!: " + str(healingPotion == 1 and healthPoints <= 6))
print("--- Phew, you have a healing potion: " + str(not (healthPoints < mCombatStrength and healingPotion == 1)))
print("--- Things are getting dangerous: " + str(healingPotion == 0 or healthPoints == 1))
print("--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

# Health status
if healthPoints >= 5:
    print("--- Your health is ok")
elif healingPotion == 1:
    healingPotion = 0
    healthPoints = 6
    print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
else:
    print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")

# Battle loop for 10 rounds
for j in range(1, 21, 2):  # range from 1 to 20 with step 2 (10 rounds total)
    input(f"Round {j}: Press Enter to continue...")

    # Hero and monster roll for the round
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    # Add dice roll to combat strength
    heroTotalStrength = combatStrength + heroRoll
    monsterTotalStrength = mCombatStrength + monsterRoll

    # Determine weapons based on rolls
    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    print(f"\nRound {j}: Hero rolled {heroRoll}, Monster rolled {monsterRoll}.")
    print(f"Hero selected: {heroWeapon}, Monster selected: {monsterWeapon}.")
    print(f"Hero Total Strength: {heroTotalStrength}, Monster Total Strength: {monsterTotalStrength}.")

    # Determine winner for the round
    if heroTotalStrength > monsterTotalStrength:
        print("Hero wins the round!")
    elif monsterTotalStrength > heroTotalStrength:
        print("Monster wins the round!")
    else:
        print("It's a tie!")

    # Battle truce condition after round 10
    if j == 11:
        print("\nBattle Truce declared in Round 11. Game Over!")
        break
