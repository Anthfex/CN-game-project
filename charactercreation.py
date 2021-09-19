warrior_statistics = [
    "Warrior",
    "Weapon type : Steel Sword and Shield",
    "max HP : 200",
    "DMG Range : 4-6",
    "Armor Rating : 5",
    "Bio - david the holy warrior of triene is a master of fighting", 
    "the dark forces of hailvaara he holds no fear as he wields his sword",
    "and shield, he instills fear into his enemies that burns deep into",
    "their dark souls"
]
archer_statistics = [
    "Archer",
    "Weapon type : Elven Bow and arrows",
    "Max HP : 150",
    "DMG Range : 2-8",
    "Armor Rating : 3",
    "Bio - clara the divine archer originates from the hidden village in the woods,",
    "she is a part of the rangers of the north and possesses a bow that gleams light",
    "of honour and justice, she never backs down from unimaginable danger,",
    "striking mercilessly from the shadows"
]
mage_statistics = [
    "Mage",
    "Weapon type : Ash staff",
    "max HP : 100",
    "DMG Range : 4-10",
    "Armor rating : 1",
    "Bio - merlin, the only mage in this region, he creates mostly mess and disfunction",
    "but occasionaly he will disply a feat of magic that reminds the locals why they rely",
    "on him on a regular basis, whereever he goes he feels compeled to try to help if he can"
]
def character_selection():
    player=input("Which champion will face this perilous journey? (W/A/M)")
    player = player.lower()
    if player == "w":
        for i in warrior_statistics:
            print(i)
        print("are you sure you want to choose this character?")
        confirmation = input("YES or NO")
        if confirmation == "y":
            hero = "David, The Holy Knight"
            print(f"You have chosen {hero}, to face Lun'Kat, The Winged Terror of the Skies!")
        elif confirmation == "n":
            character_selection()
        else:
            print("invalid selection, please try again")
            character_selection() 
    elif player == "a":
        for i in archer_statistics:
            print(i)
        print("are you sure you want to choose this character?")
        confirmation = input("YES or NO")
        if confirmation == "y":
            hero = "clara, the divine archer"
            print("you need to complete the game to unlock this character")
            character_selection()
        elif confirmation == "n":
            character_selection()
        else:
            print("invalid selection, please try again")
            character_selection()
    elif player == "m":
        for i in mage_statistics:
            print(i)
        print("are you sure you want to choose this character?")
        confirmation = input("YES or NO")
        if confirmation == "y":
            hero = "Merlin, The Elemental Sage"
            print("you need to complete the game to unlock this character")
            character_selection()
        elif confirmation == "n":
            character_selection()
        else:
            print("invalid selection, please try again")
            character_selection()
    else:
        print("Invalid input! Thats no champion!")
        character_selection()

character_selection()