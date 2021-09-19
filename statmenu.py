stat_menu_full_party_war_starter = [
    "Warrior",
    "Archer",
    "Mage",
    "Exit"
]
stat_menu_full_party_arch_starter = [
    "archer",
    "warrior",
    "mage",
    "exit"
]
stat_menu_full_party_mage_starter = [
    "mage",
    "warrior",
    "archer",
    "exit"
]
stat_menu_war_only =[
    "warrior",
    "exit"
]
stat_menu_arch_only = [
    "archer",
    "exit"
]
stat_menu_mge_only = [
    "mage",
    "exit"
]
stat_menu_war_arch = [
    "warrior",
    "archer",
    "exit"
]
stat_menu_war_mage = [
    "warrior",
    "mage",
    "exit"
]
stat_menu_arch_war = [
    "archer",
    "warrior",
    "exit"
]
stat_menu_arch_mage = [
    "archer",
    "mage",
    "exit"
]
stat_menu_mage_war = [
    "mage",
    "warrior",
    "exit"
]
stat_menu_mage_arch = [
    "mage",
    "archer",
    "exit"
]
warrior_statistics = [
    "Warrior",
    "Weapon type : Steel Sword and Shield",
    "max HP : 200",
    "DMG Range : 4-6",
    "Armor Rating : 5"
]
archer_statistics = [
    "Archer",
    "Weapon type : Elven Bow and arrows",
    "Max HP : 150",
    "DMG Range : 2-8",
    "Armor Rating : 3"
]
mage_statistics = [
    "Mage",
    "Weapon type : Ash staff",
    "max HP : 100",
    "DMG Range : 4-10",
    "Armor rating : 1"
]
def war_stats():
    for i in warrior_statistics:
        print(i)
def arch_stats():
    for i in archer_statistics:
        print(i)
def mge_stats():
    for i in mage_statistics:
        print(i)
warrior_stats = war_stats
mage_stats = mge_stats
archer_stats = arch_stats
def statistics_menu_full_party_war_starter():
    global war_stats
    global arch_stats
    global mge_stats
    global stat_menu_full_party_war_starter
    for i in stat_menu_full_party_war_starter:
        print(i)
    selection = input("which party member would you like to inspect the stats of?")
    if selection == "warrior":
        war_stats()
        statistics_menu_full_party_war_starter()
    elif selection == "archer":
        arch_stats()
        statistics_menu_full_party_war_starter()
    elif selection == "mage":
        mge_stats()
        statistics_menu_full_party_war_starter()
    elif selection == "exit":
        StopIteration
    else:
        print("invalid selection")
        statistics_menu_full_party_war_starter()
def statistics_menu_full_party_arch_starter():
    global war_stats
    global arch_stats
    global mge_stats
    global stat_menu_full_party_arch_starter
    for i in stat_menu_full_party_arch_starter:
        print(i)
    selection = input("which party member would you like to inspect the stats of?")
    if selection == "warrior":
        war_stats()
        statistics_menu_full_party_arch_starter()
    elif selection == "archer":
        arch_stats()
        statistics_menu_full_party_arch_starter()
    elif selection == "mage":
        mge_stats()
        statistics_menu_full_party_arch_starter()
    elif selection == "exit":
        StopIteration
    else:
        print("invalid selection")
        statistics_menu_full_party_arch_starter()   
def statistics_menu_full_party_mage_starter():
    global war_stats
    global arch_stats
    global mge_stats
    global stat_menu_full_party_mage_starter
    for i in stat_menu_full_party_mage_starter:
        print(i)
    selection = input("which party member would you like to inspect the stats of?")
    if selection == "warrior":
        war_stats()
        statistics_menu_full_party_mage_starter()
    elif selection == "archer":
        arch_stats()
        statistics_menu_full_party_mage_starter()
    elif selection == "mage":
        mge_stats()
        statistics_menu_full_party_mage_starter()
    elif selection == "exit":
        StopIteration
    else:
        print("invalid selection")
        statistics_menu_full_party_mage_starter()
def statistics_menu_warrior_only():
    global war_stats
    global stat_menu_war_only
    for i in stat_menu_war_only:
        print(i)
    selection = input("which party member would you like to inspect the stats of?")
    if selection == "warrior":
        war_stats()
        statistics_menu_warrior_only()
    elif selection == "exit":
        StopIteration
    else:
        print("invalid selection")
        statistics_menu_warrior_only()
def statistics_menu_archer_only():
    global arch_stats
    global stat_menu_arch_only
    for i in stat_menu_arch_only:
        print(i)
    selection = input("which party member would you like to inspect the stats of?")
    if selection == "archer":
        arch_stats()
        statistics_menu_archer_only
    elif selection == "exit":
        StopIteration
    else:
        print("invalid selection")
        statistics_menu_archer_only()
def statistics_menu_mage_only():
    global mge_stats
    global stat_menu_mge_only
    for i in stat_menu_mge_only:
        print(i)
    selection = input("which party member would you like to inspect the stats of?")
    if selection == "mage":
        mge_stats()
        statistics_menu_mage_only()
    elif selection == "exit":
        StopIteration
    else:
        print("invalid selection")
        statistics_menu_mage_only()
def statistics_menu_warrior_archer():
    global war_stats
    global arch_stats
    global stat_menu_war_arch
    for i in stat_menu_war_arch:
        print(i)
    selection = input("which party member would you like to inspect the stats of?")
    if selection == "warrior":
        war_stats()
        statistics_menu_warrior_archer()
    elif selection == "archer":
        arch_stats()
        statistics_menu_warrior_archer()
    elif selection == "exit":
        StopIteration
    else:
        print("invalid selection")
        statistics_menu_warrior_archer()
def statistics_menu_warrior_mage():
    global war_stats
    global mge_stats
    global stat_menu_war_mage
    for i in stat_menu_war_mage:
        print(i)
    selection = input("which party member would you like to inspect the stats of?")
    if selection == "warrior":
        war_stats()
        statistics_menu_warrior_mage()
    elif selection == "mage":
        mge_stats()
        statistics_menu_warrior_mage()
    elif selection == "exit":
        StopIteration
    else:
        print("invalid selection")
        statistics_menu_warrior_mage()
def statistics_menu_archer_warrior():
    global war_stats
    global arch_stats
    global stat_menu_arch_war
    for i in stat_menu_arch_war:
        print(i)
    selection = input("which party member would you like to inspect the stats of?")
    if selection == "warrior":
        war_stats()
        statistics_menu_archer_warrior()
    elif selection == "archer":
        arch_stats()
        statistics_menu_archer_warrior()
    elif selection == "exit":
        StopIteration
    else:
        print("invalid selection")
        statistics_menu_archer_warrior()
def statistics_menu_archer_mage():
    global mge_stats
    global arch_stats
    global stat_menu_arch_mage
    for i in stat_menu_arch_mage:
        print(i)
    selection = input("which party member would you like to inspect the stats of?")
    if selection == "mage":
        mge_stats()
        statistics_menu_archer_mage()
    elif selection == "archer":
        arch_stats()
        statistics_menu_archer_mage()
    elif selection == "exit":
        StopIteration
    else:
        print("invalid selection")
        statistics_menu_archer_mage()
def statistics_menu_mage_warrior():
    global war_stats
    global mge_stats
    global stat_menu_mage_war
    for i in stat_menu_mage_war:
        print(i)
    selection = input("which party member would you like to inspect the stats of?")
    if selection == "warrior":
        war_stats()
        statistics_menu_mage_warrior()
    elif selection == "mage":
        mge_stats()
        statistics_menu_mage_warrior()
    elif selection == "exit":
        StopIteration
    else:
        print("invalid selection")
        statistics_menu_mage_warrior()
def statistics_menu_mage_archer():
    global mge_stats
    global arch_stats
    global stat_menu_arch_war
    for i in stat_menu_arch_war:
        print(i)
    selection = input("which party member would you like to inspect the stats of?")
    if selection == "mage":
        mge_stats()
        statistics_menu_mage_archer()
    elif selection == "archer":
        arch_stats()
        statistics_menu_mage_archer()
    elif selection == "exit":
        StopIteration
    else:
        print("invalid selection")
        statistics_menu_mage_archer()
