import time,sys,os
import random

os.system("cls")


TGREEN = '\033[32m'
TWHITE = '\033[0m'
TBLUE = '\033[34m'
TRED ='\033[31m'

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def typingPrintFast(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03) 

def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value 


print("      .--'''--.    ...----''''''------..........------''''''---...    .--''--.\n"
"     |         |  |     _   _   ___  ___    ___   ___   ___       |  |        |\n"
"     |         '--'    | |_| | | __| |  \  /   \ | __| / __|      '--'        |\n"
"     |         |  |    | |_| | | _|  |__/  |   | | _|  \___\      |  |        |\n"
"     |         |  |    |_| |_| |___| |   \ \___/ |___| |___/      |  |        |\n"
"     |         |  |                                               |  |        |\n"
"     |         |  |           Textbased RPG by @Team Us           |  |        |\n"
"     |.--''--. |  |...----''''''------..........------''''''---...|  |.--''--.|\n"
"      '      '.--.'                                             '.--.'      '\n"
)

time.sleep(2)

print("                    |--__\n"
"                    |\n"
"                    X\n"
"     |-___         / \           |-_\n"
"     |            ~~~~~          |\n "
"    X            | .:|          X\n"
"    / \___________| O |_________/ \ \n"
"   /~~~~         |:  . |       ~~~~\ \n"
"   |.: |________| .   : |______|: .|\n"
"   |  :|.       :  ...   :     |.  |\n"
"   | .          .  |||   .        :|\n"
"   WWW____________' ' '________WWWWW\n"
"   --         ____-      ____--_\n"
)

time.sleep(1)

typingPrintFast(TGREEN +"As the darkness rises over the land of the hailvaara, the ancient will bring the demise and destruction to all light of the west and north, many have stood up and were a battle that a last hope, but that faded when there light overshadowed the darkness might they fought bravely and as shiny beacon they brought us time to find the destined hero that will light us through this era of crisis and darkness the light will shine again and keep the darkness away forever.\n")
print(TWHITE)
time.sleep(1)
town_drunk_health = 20
warrior_health = 200
wolf_health = 35
ogre_health = 50
troll_health = 50
dragon_health = 150

typingPrint(TBLUE +"Put inputs as the first letter of the action you wish to take.\n")
print(TWHITE)

def tutorial():
    global town_drunk_health
    global warrior_health
    if town_drunk_health > 0:
        typingPrint("The Town Drunk is ready for battle?\n")
        attack = input("What action will you take?\nAttack\nDefend\n")
        attack = attack.lower()
        if attack == "a":
            print("                            _\n"
"                          .!=!.\n"
"                          \===/\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                         .-----.\n"
"                     /\__:-----:__/\ \n"
"                   ./ ._. \.-./ ._. \. \n"
"                 ./ ./  -.  V  .-  \. \.\n"
"                /__/      \   /      \__\ \n"
"                          |! !|\n"
"                          |! !|\n"
"                         / . . \ \n"
"                        |!.V V.!| \n"
"                         \. V ./ \n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                           \V/\n"
"                            '"
  )
            warrior_damage = random.randint(4,6)
            typingPrint("Town Drunk took ")
            typingPrint(TRED +f"{warrior_damage} damage.\n")
            print(TWHITE)
            time.sleep(1)
            town_drunk_health = town_drunk_health - warrior_damage
            if town_drunk_health < 0:
                town_drunk_health = 0
            else:
                town_drunk_health = town_drunk_health
            typingPrint("Town Drunk has ")
            typingPrint(TGREEN +f"{town_drunk_health} HP remaining!\n")
            print(TWHITE)
            time.sleep(1)
            typingPrint("Town Drunk is confused.\n")
            time.sleep(1)
            coin_flip = random.randint(1,2)
            if coin_flip == 1:
                typingPrint("Town Drunk hit itself in confusion.\n")
                town_drunk_health -= 4
                if town_drunk_health < 0:
                    town_drunk_health = 0
                else:
                    town_drunk_health = town_drunk_health
                typingPrint("Town Drunk has ")
                typingPrint(TGREEN +f"{town_drunk_health} HP remaining!\n")
                print(TWHITE)
                typingPrint("Lucky!\n")
                print("--------------------")
                time.sleep(1)
                tutorial()
            else:
                town_drunk_attack = random.randint(10, 20)
                typingPrint("Town Drunk hits you in confusion!\n")
                typingPrint("Town Drunk deals ")
                typingPrint(TRED + f"{town_drunk_attack} damage!\n")
                print(TWHITE)
                warrior_health -= town_drunk_attack
                typingPrint("You have ")
                typingPrint(TBLUE + f"{warrior_health} HP remaining!\n")
                print(TWHITE)
                typingPrint("How Unlucky!\n")
                print("--------------------")
                time.sleep(1)
                tutorial()
        elif attack == "d":
            town_drunk_attack = random.randint(15,25)
            warrior_armour = 5
            print("           _____________________________________________\n"
  "           \-------------------------------------------/\n            "
"V_________________________________________V\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"             \_______________|         |_____________/ \n"
"             (                                       )\n"
"              (                                     )\n"
"               V                                   V\n"
"               (____________.          .___________)\n"
"                V           |          |         V\n"
"                  V         |          |        V\n"
"                   V        |          |       V\n"
"                    V       |          |      V\n"
"                     V      |          |     V\n"
"                      V     |          |    V\n"
"                       V____|__________|___V\n"
"                        \___[.________.]__/")
            typingPrint("Town Drunk attacks!\n")
            typingPrint("You defend skillfully!\n")
            time.sleep(1)
            town_drunk_attack -= warrior_armour
            typingPrint("Town drunk deals ")
            typingPrint(TRED +f"{town_drunk_attack}!\n")
            print(TWHITE)
            warrior_health = warrior_health - town_drunk_attack
            typingPrint("You have ")
            typingPrint(TBLUE + f"{warrior_health} HP remaining!\n")
            print(TWHITE)
            time.sleep(1)
            reflection = town_drunk_attack - 10
            typingPrint("You deal ")
            typingPrint(TRED + f"{reflection} in reflection damage!\n")
            print(TWHITE)
            town_drunk_health -= reflection
            if town_drunk_health <= 0:
                town_drunk_health = 0
            else:
                town_drunk_health = town_drunk_health    
            typingPrint("Town Drunk has ")
            typingPrint(TGREEN + f"{town_drunk_health} Hp remaining!\n")
            print(TWHITE)
            print("--------------------")
            time.sleep(1)
            tutorial()
        else:
            print(TRED +"Invalid Input")
            print(TWHITE)
            time.sleep(1)
            tutorial()
    else:
        typingPrint("The Town Drunk has been defeated!\n")
        warrior_health = 200
        typingPrint("The adventure continues!\n")


tutorial()
time.sleep(2)

os.system("cls")
warrior_health = 200
typingPrint(TGREEN +"The Town Drunk has been defeated!\n The adventure continues!\n")
print(TWHITE)
time.sleep(1)

print(" .------------------.  .-----------------.  .------------------.\n"
     "| .----------------. || .---------------. || .----------------.  |\n"
     "| |                | || |      --       | || |                 | |\n"
     "| |  V     V     V | || |     /  \      | || |    /\      /\   | |\n"
     "| |   V   V V   V  | || |    / /\ \     | || |   /  \    /  \  | |\n"
     "| |    V V   V V   | || |   / ---- \    | || |  /    \  /    \ | |\n"
     "| |     V     V    | || | _/ /    \ \_  | || | /      \/      \| |\n"
     "| |                | || ||___|    |___| | || |                 | |\n"
     "| |     Warrior    | || |    Archer     | || |      Mage       | |\n"
     "| '----------------' || '---------------' || '----------------'  |\n"
     " '------------------'  '-----------------'  '------------------'"
)

typingPrint("CHARACTER SELECTION:\n")
print('')
time.sleep(1)
typingPrintFast(TGREEN+ "Warrior\n"
    "Weapon type : Steel Sword and Shield\n"
    "max HP : 200\n"
    "DMG Range : 4-6\n"
    "Armor Rating : 5\n"
    "Bio - David the holy warrior of triene is a master of fighting\n"
    "the dark forces of hailvaara he holds no fear as he wields his sword\n"
    "and shield, he instills fear into his enemies that burns deep into\n"
    "their dark souls.\n")
print(TWHITE)    
time.sleep(1)
print('')
typingPrintFast(TWHITE + "Archer\n"
    "Weapon type : Elven Bow and arrows\n"
    "Max HP : 150\n"
    "DMG Range : 2-8\n"
    "Armor Rating : 3\n"
    "Bio - Clara the divine archer originates from the hidden village in the woods,\n"
    "she is a part of the rangers of the north and possesses a bow that gleams light\n"
    "of honour and justice, she never backs down from unimaginable danger,\n"
    "striking mercilessly from the shadows.\n")
print(TWHITE)
time.sleep(1)
print('')
typingPrintFast(TGREEN + "Mage\n"
    "Weapon type : Ash staff\n"
    "max HP : 100\n"
    "DMG Range : 4-10\n"
    "Armor rating : 1\n"
    "Bio - Merlin, the only mage in this region, he creates mostly mess and disfunction\n"
    "but occasionaly he will disply a feat of magic that reminds the locals why they rely\n"
    "on him on a regular basis, whereever he goes he feels compeled to try to help if he can.\n")
print(TWHITE)
time.sleep(1)
print('')

def character_selection():
    player=typingInput("Which champion will face this perilous journey? (W/A/M)")
    player = player.lower()
    if player == "w":
        typingPrint("Are you sure you want to choose this character?")
        confirmation = input("YES or NO")
        if confirmation == "y":
            hero = "David, The Holy Knight"
            typingPrint(f"You have chosen {hero}, to face Lun'Kat, The Winged Terror of the Skies!")
        elif confirmation == "n":
            character_selection()
        else:
            typingPrint("Invalid selection, please try again")
            character_selection() 
    elif player == "a":
        typingPrint("Are you sure you want to choose this character?")
        confirmation = input("YES or NO")
        if confirmation == "y":
            hero = "clara, the divine archer"
            typingPrint("You need to complete the game to unlock this character\n")
            character_selection()
        elif confirmation == "n":
            character_selection()
        else:
            typingPrint("Invalid selection, please try again")
            character_selection()
    elif player == "m":
        typingPrint("Are you sure you want to choose this character?")
        confirmation = input("YES or NO")
        if confirmation == "y":
            hero = "Merlin, The Elemental Sage"
            typingPrint("You need to complete the game to unlock this character\n")
            character_selection()
        elif confirmation == "n":
            character_selection()
        else:
            typingPrint("Invalid selection, please try again")
            character_selection()
    else:
        typingPrint("Invalid input! Thats no champion!\n")
        character_selection()
 
character_selection()

time.sleep(2)
os.system("cls")
print("            /\             //\n"
"            \ \           _!_\n"
"             \ \         /___\ \n"
"              \ \        [+++]\n"
"               \ \    _ _\^^^/_ _\n"
"                \ \/ (    '-' ( )\n"
"                /( \/  | {&}  /\ \ \n"
"                  \   / \    /  > )\n"
"                   '''   >::; -''''''-.\n"
"                        /::: /         \ \n"
"                       /  /||    {&}   |\n"
"                      (  /  (\         /\n"
"                      / /    \*-.___.-'\n"
"                    _/ /      \ \ \n"
"                   /___|     /___|\n"
)
typingPrintFast(TGREEN +"As Dave the holy knight enter the forest of dark oaths he sees the\n"
"treeline come into focus and the dark feeling of foreboding awaits him if he enters unprepared\n"
"so he readies him self to face any danger he may face he hears howls and clenches his sword.\n")
print(TWHITE)
print('')
print('')
time.sleep(2)
typingPrint(TGREEN+"There  is a sound from behind and in front of you hear what do you do...\n")
time.sleep(1)
typingPrint("An arrow flies past and you see a wolf fall down I lend you my bow warrior of light.\n")
typingPrint("Warrior meets Archer.\n")
typingPrint(TGREEN+"I am Dave the holy night of trine these enemies dont stand a chance against our combined attack they both ready their weapons. I am Clara we wont fall here.\n")
time.sleep(1)
typingPrint("So we all will face this darkness together I dave the holy knight of trien pledge my self to the cause, I clara give my bow to this cause, I rinceword wants to go home but I offer my magic they form the heroes of trein as lightening forms in the sky we are ready.\n")
print(TWHITE)
time.sleep(2)
print("                                        __\n"
"                                      .d$$b\n"
"                                    .' TO$;\ \n"
"                                   /  : TP._;\n"
"                                  / _.;  :Tb|\n"
"                                 /   /   ;j$j\n"
"                             _.-''      d$$$$\n"  
"                           .' ..       d$$$$;\n"
"                          /  /P'      d$$$$P.  |\ \n"
"                         /   ''      .d$$$P' |\^''1\n"
"                       .'            'T$P^''''''  :\n"
"                   ._.'      _.'                  ;\n"
"                '.-''.-'-' ._.       _.-''    .-''\n"    
"              '.-''_____  ._                .-''\n"
"            -(.g$$$$$$$b.                  .'\n"
"             ''''^^T$$$P^)               .(:\n"
"                 _/  -'' /.'            /:/;\n"
"              ._.'-''-' '')/            /;/;\n"
"           '-.-''..--''' ''/            /  ;\n"
"          .-'' ..--'''     -'              :\n"
"          ..--'''--.-''      (\         ..-(\ \n"
"            ..--'''            '-\(\/;''\n"
"              _.                     :\n"
"                                     ;'-\n"
"                                    :\ \n"
"                                    ;\n"
)

def fight_wolf():
    global warrior_health
    global wolf_health
    wolf_damage = random.randint(10,15)
    if wolf_health > 0 and warrior_health > 0:
        typingPrint("The Wolf Pack is ready for battle!\n")
        attack = typingInput("What action will you take?\nAttack\nDefend\n")
        attack = attack.lower()
        if attack == "a":
            print("                            _\n"
"                          .!=!.\n"
"                          \===/\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                         .-----.\n"
"                     /\__:-----:__/\ \n"
"                   ./ ._. \.-./ ._. \. \n"
"                 ./ ./  -.  V  .-  \. \.\n"
"                /__/      \   /      \__\ \n"
"                          |! !|\n"
"                          |! !|\n"
"                         / . . \ \n"
"                        |!.V V.!| \n"
"                         \. V ./ \n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                           \V/\n"
"                            '"
  )
            warrior_damage = random.randint(7,10)
            typingPrint("Wolf Pack took ")
            typingPrint(TRED +f"{warrior_damage} damage!\n")
            print(TWHITE)
            time.sleep(1)
            wolf_health -= warrior_damage
            if wolf_health < 0:
                wolf_health = 0
            else:
                wolf_health = wolf_health
            typingPrint("Wolf Pack has ")
            typingPrint(TGREEN +f"{wolf_health} HP remaining!\n")
            print(TWHITE)
            time.sleep(1)
            wolf_damage = random.randint(10,15)
            wolf_attack_order = random.randint(2,4)
            for i in range(wolf_attack_order):
                print(f"Wolf Pack deals {wolf_damage} damage!")
            wolf_damage *= wolf_attack_order
            warrior_health -= wolf_damage
            if warrior_health < 0:
                warrior_health = 0
            else:
                warrior_health = warrior_health
            typingPrint("You have ")
            typingPrint(TBLUE +f"{warrior_health} HP remaining!\n")
            print(TWHITE)
            typingPrint("--------------------\n")
            time.sleep(1)
            fight_wolf()
        elif attack == "d":
            print("           _____________________________________________\n"
  "           \-------------------------------------------/\n            "
"V_________________________________________V\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"             \_______________|         |_____________/ \n"
"             (                                       )\n"
"              (                                     )\n"
"               V                                   V\n"
"               (____________.          .___________)\n"
"                V           |          |         V\n"
"                  V         |          |        V\n"
"                   V        |          |       V\n"
"                    V       |          |      V\n"
"                     V      |          |     V\n"
"                      V     |          |    V\n"
"                       V____|__________|___V\n"
"                        \___[.________.]__/")
            warrior_armour = 5
            typingPrint("The Wolf Packs Attacks!\n")
            typingPrint("You defend cautiosly!\n")
            time.sleep(1)
            wolf_damage = random.randint(10,15)
            wolf_damage -= warrior_armour
            wolf_attack_order = random.randint(2,4)
            for i in range(wolf_attack_order):
                print("Wolf Pack deals ") 
                print(TRED+f"{wolf_damage} damage!")
                print(TWHITE)
            wolf_damage *= wolf_attack_order
            warrior_health -= wolf_damage
            if warrior_health < 0:
                warrior_health = 0
            else:
                warrior_health = warrior_health
            typingPrint("You have ") 
            typingPrint(TBLUE +f"{warrior_health} HP remaining!\n")
            print(TWHITE)
            time.sleep(1)
            reflection = int(wolf_damage/2)
            typingPrint("You have dealt ")
            typingPrint(TRED +f"{reflection} reflection damage!\n")
            print(TWHITE)
            wolf_health -= reflection
            if wolf_health < 0:
                wolf_health = 0
            else:
                wolf_health = wolf_health
            typingPrint("The Wolf Pack have ") 
            typingPrint(TGREEN +f"{wolf_health} HP remaining!\n")
            print(TWHITE)
            typingPrint("You ") 
            typingPrint(TGREEN +"heal 5 HP!")
            print(TWHITE)
            warrior_health += 5
            typingPrint("You have ")
            typingPrint(TBLUE +f"{warrior_health} HP remaining!\n")
            print(TWHITE)
            typingPrint("--------------------\n")
            time.sleep(1)
            fight_wolf()
        else:
            print(TRED+"Invalid Input")
            print(TWHITE)
            typingPrint("--------------------\n")
            time.sleep(1)
            fight_wolf()
    elif wolf_health == 0 and warrior_health > 0:
        typingPrint("The Wolf Pack have been defeated!\n")
        typingPrint("The adventure continues!\n")
        typingPrint("--------------------\n")
        warrior_health = 200
    else:
        typingPrint("You have been defeated by the mighty wolf pack!\n")
        typingInput("Press any button to get your revenge!\n")
        warrior_health = 200
        fight_wolf()

fight_wolf()  

time.sleep(3)
os.system("cls")

typingPrint(TGREEN +"The warrior and the archer continues to walk through the forest...\nThey hear someting.\n")
time.sleep(1)   
typingPrint("Oh no! It's an Ogre!\n")
print(TWHITE)
time.sleep(1)
print("                ______                   ______                 ______\n"  
"               ( O  o )                 ( O  o )               ( O  o )              \n"
"              /    0    \              /    0    \            /    0    \ \n"
"             / / |    |\ \            / / |    |\ \          / / |    |\ \ \n"
"            ///\  |  |  ('')         ///\  |  |  ('')       ///\  |  |  ('')\n"
"                   ||                       ||                     ||\n"
"                  /  \                     /  \                   /  \ \n"
"                 _|  |_                   _|  |_                 _|  |_\n"
)
time.sleep(1)
turn = 1
def fight_ogre():
    global warrior_health
    global ogre_health
    global turn
    turn += 1
    if turn%2 == 0:
        if ogre_health > 0 and warrior_health > 0:
            typingPrint("The Ogre Lord is ready for battle!\n")
            attack = typingInput("What action will you take?\nAttack\nDefend\n")
            attack = attack.lower()
            if attack == "a":
                print("                            _\n"
"                          .!=!.\n"
"                          \===/\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                         .-----.\n"
"                     /\__:-----:__/\ \n"
"                   ./ ._. \.-./ ._. \. \n"
"                 ./ ./  -.  V  .-  \. \.\n"
"                /__/      \   /      \__\ \n"
"                          |! !|\n"
"                          |! !|\n"
"                         / . . \ \n"
"                        |!.V V.!| \n"
"                         \. V ./ \n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                           \V/\n"
"                            '"
  )
                warrior_damage = random.randint(9,14)
                typingPrint("Ogre Lord took ")
                typingPrint(TRED +f"{warrior_damage} damage!\n")
                print(TWHITE)
                time.sleep(1)
                ogre_health -= warrior_damage
                if ogre_health < 0:
                    ogre_health = 0
                else:
                    ogre_health = ogre_health
                typingPrint("Ogre Lord has ")
                typingPrint(TGREEN+f"{ogre_health} HP remaining!\n")
                print(TWHITE)
                time.sleep(1)
                ogre_damage = random.randint(30,60)
                typingPrint("Ogre Lord deals ")
                typingPrint(TRED +f"{ogre_damage} damage!\n")
                print(TWHITE)
                warrior_health -= ogre_damage
                if warrior_health < 0:
                    warrior_health = 0
                else:
                    warrior_health = warrior_health
                typingPrint("You have ")
                typingPrint(TBLUE +f"{warrior_health} HP remaining!\n")
                print(TWHITE)
                print("--------------------\n")
                time.sleep(1)
                fight_ogre()
            elif attack == "d":
                print("           _____________________________________________\n"
  "           \-------------------------------------------/\n            "
"V_________________________________________V\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"             \_______________|         |_____________/ \n"
"             (                                       )\n"
"              (                                     )\n"
"               V                                   V\n"
"               (____________.          .___________)\n"
"                V           |          |         V\n"
"                  V         |          |        V\n"
"                   V        |          |       V\n"
"                    V       |          |      V\n"
"                     V      |          |     V\n"
"                      V     |          |    V\n"
"                       V____|__________|___V\n"
"                        \___[.________.]__/")
                warrior_armour = 10
                typingPrint("The Ogre Lord Attacks!\n")
                typingPrint("You defend desperately!\n")
                time.sleep(1)
                ogre_damage = random.randint(30,60)
                ogre_damage -= warrior_armour
                typingPrint("The Ogre Lord deals ")
                typingPrint(TRED +f"{ogre_damage} damage!\n")
                print(TWHITE)
                warrior_health -= ogre_damage
                if warrior_health < 0:
                    warrior_health = 0
                else:
                    warrior_health = warrior_health
                typingPrint("You have ")
                typingPrint(TBLUE +f"{warrior_health} HP remaining!\n")
                print(TWHITE)
                time.sleep(1)
                reflection = int(ogre_damage/2)
                typingPrint("You have dealt ")
                typingPrint(TRED +f"{reflection} reflection damage!\n")
                print(TWHITE)
                ogre_health -= reflection
                if ogre_health < 0:
                    ogre_health = 0
                else:
                    ogre_health = ogre_health
                typingPrint("Ogre Lord has ")
                typingPrint(TGREEN +f"{ogre_health} HP remaining!\n")
                print(TWHITE)
                typingPrint("You ")
                typingPrint(TGREEN +"heal 5 HP!")
                print(TWHITE)
                warrior_health += 5
                typingPrint("You have ")
                typingPrint(TBLUE +f"{warrior_health} HP remaining!\n")
                print(TWHITE)
                print("--------------------\n")
                time.sleep(1)
                fight_ogre()
            else:
                print(TRED +"Invalid Input")
                print(TWHITE)
                print("--------------------\n")
                time.sleep(1)
                fight_ogre()
        elif ogre_health == 0 and warrior_health > 0:
            typingPrint("The Ogre Lord have been defeated!\n")
            typingPrint("The adventure continues!\n")
            print("--------------------\n")
            warrior_health = 200
        else:
            typingPrint("You have been defeated by the glorious Ogre Lord!\n")
            typingInput("Press any button to get your revenge!\n")
            warrior_health = 200
            fight_ogre()
    else:
        typingPrint("You attack the Ogre Lord!\n")
        warrior_damage = random.randint(9,14)
        typingPrint("Ogre Lord took ")
        typingPrint(TRED +f"{warrior_damage} damage!\n")
        print(TWHITE)
        time.sleep(1)
        ogre_health -= warrior_damage
        if ogre_health < 0:
            ogre_health = 0
        else:
            ogre_health = ogre_health
        typingPrint("Ogre Lord has ")
        typingPrint(TGREEN +f"{ogre_health} HP remaining!\n")
        print(TWHITE)
        typingPrint("The Ogre Lord is charging up his attack!\n")
        print("--------------------\n")
        fight_ogre()
        
fight_ogre()

time.sleep(3)
os.system("cls")

typingPrint(TGREEN +"They fought bravely and win the fight against the Ogre.\n"
"But thats not the end...\n")
time.sleep(1)
typingPrint("The forest trolls comes out, and you roll out the way and guard yourself.\n")
print(TWHITE)
time.sleep(1)
print("       ''''''''''''             ''''''''''''            ''''''''''''\n"
"        \(.\  /.)/               \(.\  /.)/              \(.\  /.)/\n"
"         \  ..  /                 \  ..  /                \  ..  /\n"
"          \ t--/                   \ t--/                  \ t--/\n"
"           \__/                     \__/                    \__/\n"
)

print("       ''''''''''''             ''''''''''''            ''''''''''''\n"
"        \(.\  /.)/               \(.\  /.)/              \(.\  /.)/\n"
"         \  ..  /                 \  ..  /                \  ..  /\n"
"          \ t--/                   \ t--/                  \ t--/\n"
"           \__/                     \__/                    \__/\n"
)

time.sleep(1)
def fight_forest_troll():
    global warrior_health
    global troll_health
    troll_damage = random.randint(10,15)
    if troll_health > 0 and warrior_health > 0:
        typingPrint("The Forest Trolls are ready for battle!\n")
        attack = typingInput("What action will you take?\nAttack\nDefend\n")
        attack = attack.lower()
        if attack == "a":

            warrior_damage = random.randint(7,10)
            typingPrint("The Forest Trolls took ")
            typingPrint(TRED +f"{warrior_damage} damage!\n")
            print(TWHITE)
            time.sleep(1)
            troll_health -= warrior_damage
            if troll_health < 0:
                troll_health = 0
            else:
                troll_health = troll_health
            typingPrint("Forest Trolls have ")
            typingPrint(TGREEN +f"{troll_health} HP remaining!\n")
            print(TWHITE)
            time.sleep(1)
            troll_damage = random.randint(10,15)
            for i in range(2):
                typingPrint("Forest Trolls deal ")
                typingPrint(TRED +f"{troll_damage} damage!\n")
                print(TWHITE)
            troll_damage *= 2
            warrior_health -= troll_damage
            if warrior_health < 0:
                warrior_health = 0
            else:
                warrior_health = warrior_health
            typingPrint("You have ")
            typingPrint(TBLUE+f"{warrior_health} HP remaining!\n")
            print(TWHITE)
            print("--------------------")
            time.sleep(1)
            fight_forest_troll()
        elif attack == "d":
            print("           _____________________________________________\n"
  "           \-------------------------------------------/\n            "
"V_________________________________________V\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"             \_______________|         |_____________/ \n"
"             (                                       )\n"
"              (                                     )\n"
"               V                                   V\n"
"               (____________.          .___________)\n"
"                V           |          |         V\n"
"                  V         |          |        V\n"
"                   V        |          |       V\n"
"                    V       |          |      V\n"
"                     V      |          |     V\n"
"                      V     |          |    V\n"
"                       V____|__________|___V\n"
"                        \___[.________.]__/")
            warrior_armour = 7
            typingPrint("The Forest Trools Attacks!\n")
            typingPrint("You defend skeptically!\n")
            time.sleep(1)
            troll_damage = random.randint(10,15)
            troll_damage -= warrior_armour
            for i in range(4):
                typingPrint("Forest Trolls have dealt ")
                typingPrint(TRED +f"{troll_damage} damage!\n")
                print(TWHITE)
            troll_damage *= 4
            warrior_health -= troll_damage
            if warrior_health < 0:
                warrior_health = 0
            else:
                warrior_health = warrior_health
            typingPrint("You have ")
            typingPrint(TGREEN +f"{warrior_health} HP remaining!\n")
            print(TWHITE)
            time.sleep(1)
            reflection = int(troll_damage/2)
            typingPrint("You have dealt ")
            typingPrint(TRED +f"{reflection} reflection damage!\n")
            print(TWHITE)
            troll_health -= reflection
            if troll_health < 0:
                troll_health = 0
            else:
                troll_health = troll_health
            typingPrint("The Forest Trolls have ")
            typingPrint(TGREEN +f"{troll_health} HP remaining!\n")
            print(TWHITE)
            typingPrint("You ")
            typingPrint(TGREEN +"heal 8 HP!"),TWHITE
            warrior_health += 7
            typingPrint("You have ")
            typingPrint(TBLUE +f"{warrior_health} HP remaining!\n")
            print(TWHITE)
            print("--------------------")
            time.sleep(1)
            fight_forest_troll()
        else:
            print(TRED +"Invalid Input")
            print(TWHITE)
            print("--------------------")
            time.sleep(1)
            fight_forest_troll()
    elif troll_health == 0 and warrior_health > 0:
        typingPrint("The Forest Trolls have been defeated!\n")
        typingPrint("The adventure continues!\n")
        print("--------------------")
        warrior_health = 200
    else:
        typingPrint("You have been defeated by the militaristic Forest Trolls!\n")
        typingInput("Press any button to get your revenge!\n")
        warrior_health = 200
        fight_forest_troll()

fight_forest_troll()

time.sleep(3)
os.system("cls")

typingPrint(TGREEN +"The warrior come across a castle with a light trying to get your interest, but a massive shadow on the bridge of the souls which way will you go?\n")
print(TWHITE)
time.sleep(1)
print("                    |--__\n"
"                    |\n"
"                    X\n"
"     |-___         / \           |-_\n"
"     |            ~~~~~          |\n "
"    X            | .:|          X\n"
"    / \___________| O |_________/ \ \n"
"   /~~~~         |:  . |       ~~~~\ \n"
"   |.: |________| .   : |______|: .|\n"
"   |  :|.       :  ...   :     |.  |\n"
"   | .          .  |||   .        :|\n"
"   WWW____________' ' '________WWWWW\n"
"   --         ____-      ____--_\n"
"              \   \      \   \ \n"
"               \ - \      \ - \ \n"
"                \   \      \   \ \n"
"                 \ - \      \ - \ \n"
"                  \   \      \   \ \n"
"                    ^           ^\n"
"                   Left        Right\n"
)

def path_choice():
    typingPrint(TGREEN +"You have come to fork in the road, which path will you choose? The path to the left leads to forboding bridge, the right path leads to a strangley alluring light.\n")
    print(TWHITE)
    answer=typingInput("Will you go left (L) or right(R): \n")
    answer=answer.lower()
    if answer == "l":
       typingPrint("You pass through the gate unhindered and welcomed inn by a mysterious force bekoning you forward.\n")
    elif answer == "r":
       typingPrintFast("You head to the light and see a door you open it and see a grimmare of unbeatable pun or terrible take your pick held by Jon the pun master smirking and grinning like he knew ypu was coming mahhhhhhhhhhhhhh.\n"
       "He is a level 10 pun master sorcerer supreme of all trien he says vailed line of pun and attack who speaks the unspeakable puns that are lost through time thought to bad to say he broke that and used as a weapon, he looked in the forbiben tomes of trien acient pun masters of history they cant hold to pun to power of jon and became the punmaster and stands alone at the top of pun mountian making sure the sumit is attainible through hard work and bad timing i stiming is so bad internet lag has better timing bbut he covets this power and gaurds the entrance of secrets yet to be defeated no pun can beat him only pun can slay him is forggotten for a reason.")
    else:
     print("Invalid Input")
     print("--------------------")
     time.sleep(1)
    

path_choice()

time.sleep(3)
os.system("cls")

typingPrintFast(TGREEN +"You see a dragon sleeping on the floor with piles of gold and the lost ring of power this item yet to make dlc you see the dragon hasnt noticed you so you draw your sword and stab it he doesnt wake up it doesnt seem to have a affect on him.\n")
print(TWHITE)
time.sleep(1)
print("                          |>                         |>\n"
"                          |                          |\n"
"        .   .   ,   .-._.-._.-._.-.            .-._.-._.-._.-.\n" 
"        | \_/ \./|  ,|_____________|      ,     |_____________|\n"  
"      /  .---.   -/( |           | /\  /   \  , |           |\n"
"      /  /  _  \  //(/|   ||      |;  \;     ;/ \|   ||      |\n"
"     /  :  (0)  ;  )/ |           |_-_-_-_-_-_-_-|           |          /|\n"
"    /   \       /     |           |     _____    |           |         ((\n"
"   |.   '-----'   )  |       ||  |    |||||||   |           |          \ \ \n"
"     |/\/\/\/\/   /   |           |    |||||||   |      ||   |\         ; |\n"
"     \___________/    |           |    |||||||   |           |''---...-' _-\n"
"          ____.--'    |           |    |||||||   |           |   __.,.-''\n"
"         (((( ,.....__|___________|____|||||||___|________1db|'''\n")
time.sleep(1)
def fight_dragon():
    global warrior_health
    global dragon_health
    dragon_damage = random.randint(50,80)
    if dragon_health > 0 and warrior_health > 0:
        typingPrint("The Dragon is ready for battle!\n")
        attack = input("What action will you take?\nAttack\nDefend\n")
        attack = attack.lower()
        if attack == "a":
            print("                            _\n"
"                          .!=!.\n"
"                          \===/\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                          |>X<|\n"
"                         .-----.\n"
"                     /\__:-----:__/\ \n"
"                   ./ ._. \.-./ ._. \. \n"
"                 ./ ./  -.  V  .-  \. \.\n"
"                /__/      \   /      \__\ \n"
"                          |! !|\n"
"                          |! !|\n"
"                         / . . \ \n"
"                        |!.V V.!| \n"
"                         \. V ./ \n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                          || ||\n"
"                           \V/\n"
"                            '"
  )
            warrior_damage = random.randint(7,10)
            typingPrint("The Dragon took ") 
            typingPrint(TRED+f"{warrior_damage} damage!\n")
            print(TWHITE)
            time.sleep(1)
            dragon_health -= warrior_damage
            if dragon_health  < 0:
                dragon_health  = 0
            else:
                dragon_health  = dragon_health 
            typingPrint("Dragon has ")
            typingPrint(TGREEN +f"{dragon_health } HP remaining!\n")
            print(TWHITE)
            time.sleep(1)
            dragon_damage = random.randint(50,80)
            warrior_health -= dragon_damage
            typingPrint("The dragon deals ")
            typingPrint(TRED+ f"{dragon_damage} damage\n")
            print(TWHITE)
            if warrior_health < 0:
                warrior_health = 0
            else:
                warrior_health = warrior_health
            typingPrint("You have ") 
            typingPrint(TBLUE+f"{warrior_health} HP remaining!\n")
            print(TWHITE)
            print("--------------------")
            time.sleep(1)
            fight_dragon()
        elif attack == "d":
            print("           _____________________________________________\n"
  "           \-------------------------------------------/\n            "
"V_________________________________________V\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"            |                |         |              |\n"
"             \_______________|         |_____________/ \n"
"             (                                       )\n"
"              (                                     )\n"
"               V                                   V\n"
"               (____________.          .___________)\n"
"                V           |          |         V\n"
"                  V         |          |        V\n"
"                   V        |          |       V\n"
"                    V       |          |      V\n"
"                     V      |          |     V\n"
"                      V     |          |    V\n"
"                       V____|__________|___V\n"
"                        \___[.________.]__/")
            warrior_armour = 5
            typingPrint("The Dragon Attacks!\n")
            typingPrint("You defend cautiosly!\n")
            time.sleep(1)
            dragon_damage = random.randint(50,80)
            dragon_damage-= warrior_armour
            warrior_health -= dragon_damage
            typingPrint("The dragon deals ")
            typingPrint(TRED+ f"{dragon_damage} damage.\n")
            print(TWHITE)
            if warrior_health < 0:
                warrior_health = 0
            else:
                warrior_health = warrior_health
            typingPrint("You have ")
            typingPrint(TBLUE +f"{warrior_health} HP remaining!\n")
            print(TWHITE)
            time.sleep(1)
            reflection = int(dragon_damage/2)
            typingPrint("You have dealt ")
            typingPrint(TRED+ f"{reflection} reflection damage!\n")
            print(TWHITE)
            dragon_health -= reflection
            if dragon_health < 0:
                dragon_health = 0
            else:
                dragon_health = dragon_health
            typingPrint("The Dragon has ")
            typingPrint(TGREEN+f"{dragon_health} HP remaining!\n")
            print(TWHITE)
            typingPrint("You heal 5 HP!")
            warrior_health += 5
            typingPrint("You have ")
            typingPrint(TBLUE+f"{warrior_health} HP remaining!\n")
            print(TWHITE)
            print("--------------------")
            time.sleep(1)
            fight_dragon()
        else:
            print(TRED +"Invalid Input\n")
            print(TWHITE)
            print("--------------------")
            time.sleep(1)
            fight_dragon()
    elif dragon_health == 0 and warrior_health > 0:
        typingPrint("The Dragon have been defeated!\n")
        typingPrint("You feel a emotional overflow of joy as it's lifeless body hits the ground!\n")
        print("--------------------")
    else:
        typingPrint("You have been defeated by the castle-sized Dragon!\n")
        typingInput("Press any button to get your revenge!\n")
        warrior_health = 200
        fight_dragon()

fight_dragon()

time.sleep(3)
os.system("cls")
def game_end_decider():
    coin_flip = random.randint(1,3)
    if coin_flip == 1:
        print("you take the princess up on her offer")
        print("after a long hard journey")
        print("you return with the princess back to")
        print("the town of Trien, you enter the castle ready to")
        print("meet the king, however just as the doors were about")
        print("open, you hear a very familiar groan, the doors")
        print("swing open and to your suprise")
        print(".....................")
        print(".....................")
        print("there sat apon the throne was none other than")
        print("Tim the town drunk")
        print(".....................")
        print("david went on to recieve incredible merit for his")
        print("actions and was given a new position as a royal knight")
        print("he continued to adventure on into the great unknown")
        print("for the many years that followed")
        print("THE END")
    else:
        print("suddenly out of nowhere you hear the whistle")
        print("of an arrow in flight, before you have a chance")
        print("to react the arrow pierces straight through you armour")
        print("you fall to the floor in unimaginable pain")
        print("you look down to inspect were the rrow has struck you")
        print("the arrow has gone through your knee")
        print("out of the shadows your attacker starts to emerge")
        print("..................")
        print("..................")
        print("one of the towns guards emerges.")
        print("''this serves you adventurers right, i have to")
        print("watch you all going on your cool adventures")
        print("while i'm sat waiting for the bi-monthly")
        print("bandit raid.''")
        print("the guard continues to rant but you pass out from")
        print("the pain")
        print("..................")
        print("..................")
        print("..................")
        print("you awake hours later, the sky is starting to go dark")
        print("the princess and the guard have left.")
        print("you drag yourself onto your feet.")
        print("and start to make your way back to Trien")
        print("..................")
        print("david went on to enroll as a city guard in Trien")
        print("he never saw the guard who shot him ever again")
        print("he went on to gain a dislike to all adventurers")
        print("always making them aware of his past life as a adventurer")
        print("..................")
        print("and then he took an arrow to the knee...")
        print("THE END")
game_end_decider()