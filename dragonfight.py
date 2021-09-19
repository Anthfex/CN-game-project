import random
import time
dragon_health = 150
warrior_health = 200
def fight_dragon():
    global warrior_health
    global dragon_health
    dragon_damage = random.randint(50,80)
    if dragon_health > 0 and warrior_health > 0:
        print("The Dragon is ready for battle!")
        attack = input("What action will you take?\nAttack\nDefend\n")
        attack = attack.lower()
        if attack == "a":
            warrior_damage = random.randint(15,25)
            print(f"The Dragon took {warrior_damage} damage!")
            time.sleep(1)
            dragon_health -= warrior_damage
            if dragon_health < 0:
                dragon_health = 0
            else:
                dragon_health = dragon_health
            print(f"Dragon has {dragon_health}HP remaining!")
            time.sleep(1)
            dragon_damage = random.randint(50,80)
            warrior_health -= dragon_damage
            print(f"The dragon deals {dragon_damage} damage")
            if warrior_health < 0:
                warrior_health = 0
            else:
                warrior_health = warrior_health
            print(f"You have {warrior_health}HP remaining!")
            print("--------------------")
            time.sleep(1)
            fight_dragon()
        elif attack == "d":
            warrior_armour = 5
            print("The Dragon Attacks!")
            print("You defend cautiosly!")
            time.sleep(1)
            dragon_damage = random.randint(50,80)
            dragon_damage -= warrior_armour
            warrior_health -= dragon_damage
            print(f"The dragon deals {dragon_damage} damage")
            if warrior_health < 0:
                warrior_health = 0
            else:
                warrior_health = warrior_health
            print(f"You have {warrior_health}HP remaining!")
            time.sleep(1)
            reflection = int(dragon_damage/2)
            print(f"You have dealt {reflection} reflection damage!")
            dragon_health -= reflection
            if dragon_health < 0:
                dragon_health = 0
            else:
                dragon_health = dragon_health
            print(f"The Dragon has {dragon_health}HP remaining!")
            print("You heal 5HP!")
            warrior_health += 5
            print(f"You have {warrior_health}HP remaining!")
            print("--------------------")
            time.sleep(1)
            fight_dragon()
        else:
            print("Invalid Input")
            print("--------------------")
            time.sleep(1)
            fight_dragon()
    elif dragon_health == 0 and warrior_health > 0:
        print("The Dragon have been defeated!")
        print("You feel a emotional overflow of joy as it's lifeless body hits the ground!")
        print("--------------------")
    else:
        print("You have been defeated by the castle-sized Dragon!")
        input("Press any button to collect your puns and try again!")
        fight_dragon()
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
fight_dragon()
print("the princess practically sprints over to you screaming crying")
print("''do you have any idea how long i've been here,")
print("i came here with some other adventurers months ago,")
print("i don't care anymore but if you ever find a thief,")
print("called kazuma, tell him lady aqua is angry with him.''")
print("the princess starts to calm down and take a large breath.")
print("''now i'm going to go home are you coming with?''")
game_end_decider()
