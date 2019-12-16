import array as arr
import random

########################################################################################################################
# All lists containing data that can be generated for an NPC. Consider altering the program to access these list from
# .txt files or database vs the current listing of data below, in the future.

Races = ['Human', 'Dwarf', 'Half-Elf', 'Dark-Elf', 'High-Elf', 'Wood-Elf', 'Gnome', 'Halfling', 'Half-Orc']

Classes = ['Fighter', 'Rogue', 'Ranger', 'Monk', 'Paladin', 'Cleric', 'Wizard', 'Sorcerer', 'Druid', 'Warlock', 'Bard']

Stats = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

Professions = ['Combat_Professions', 'Labor_Professions', 'Service_Professions']
Combat_Professions = ['Fighter', 'Mercenary', 'Hunter', 'Soldier', 'Knight']
Labor_Professions = ['Farmer', 'Miller', 'Miner', 'Lumberjack', 'Laborer']
Service_Professions = ['Baker', 'Carpenter', 'Blacksmith', 'Tanner', 'Merchant']
#Villian_Professions = ['Bandit', 'Cultist', 'Thief', 'Assassin', 'Savage']

Equipment_Type = ['Armors', 'Weapons', 'Backup_Weapons']

Armors = ['Robe', 'Padded Armor', 'Leather Armor', 'Studded Armor', 'Hide Armor', 'Chain Shirt', 'Scale Mail', 'Breastplate',
          'Half Plate', 'Ring Mail', 'Chain Mail', 'Splint Mail', 'Plate Armor']

Weapons = ['Staff', 'Club', 'Dagger', 'Short Bow', 'Short Sword', 'Hand Axe']

Backup_Weapons = ['Staff', 'Club', 'Dagger', 'Short Bow', 'Short Sword', 'Hand Axe']

Loot = []

Abilities = []

########################################################################################################################
# Chooses a random Race from the race list. Non-weighted

def generate_Race( Races ):
    NPC_Race = Races[random.randint(0, len(Races)-1)]
    print(NPC_Race)
    #print("test")

    return NPC_Race

########################################################################################################################
# Chooses a random class from the class list. Non-weighted

def generate_Class( Classes ):
    NPC_Class = Classes[random.randint(0, len(Classes)-1)]
    print(NPC_Class)

    return NPC_Class

########################################################################################################################
# Rolls a D6 four times and then drops the lowest value before returning the final roll total

def stat_Roll():
    rolls = [0] * 4
    for i in range(len(rolls)):
        rolls[i] = (random.randint(1,6))

    #print(rolls)
    #print(min(rolls))

    Final_roll = (rolls[0] + rolls[1] + rolls[2] + rolls[3] - min(rolls))

    #print(Final_roll)

    return Final_roll

########################################################################################################################
# Generates the stats for the generated NPC by calling stat_Roll(). After the stats are distributed, checks the
# race of the character and then makes racial adjustments to the statistics before printing and returning the stats.
# Stats are returned as a list in the order of Str,Dex,Con,Int,Wis,Cha


def generate_Stats( Stats, Race ):
    NPC_Str = stat_Roll()
    NPC_Dex = stat_Roll()
    NPC_Con = stat_Roll()
    NPC_Int = stat_Roll()
    NPC_Wis = stat_Roll()
    NPC_Cha = stat_Roll()


    if Race == "Dwarf":
        NPC_Con += 2

    if Race == "Human":
        NPC_Str += 1
        NPC_Dex += 1
        NPC_Con += 1
        NPC_Int += 1
        NPC_Wis += 1
        NPC_Cha += 1

    if Race == "Gnome":
        NPC_Int += 2
    if Race == "Halfling":
        NPC_Dex += 2
    if Race == "Half-Orc":
        NPC_Str += 2
        NPC_Con += 1
    #if Race == "Half-Elf":
    if Race == "Wood-Elf" or "Dark-Elf" or "High-Elf":
        NPC_Dex += 2





    NPC_Stats = [NPC_Str, NPC_Dex, NPC_Con, NPC_Int, NPC_Wis, NPC_Cha]
    print("Strength -", NPC_Str)
    print("Dexterity -", NPC_Dex)
    print("Constitution -", NPC_Con)
    print("Intelligence -", NPC_Int)
    print("Wisdom -", NPC_Wis)
    print("Charisma -", NPC_Cha)

    return NPC_Stats

########################################################################################################################
# Chooses a random Profession type, then chooses a random Specific Profession from the list within the chosen Profession
# type. For example, the chosen Profession type could be "Labor Profession", the function would then randomly choose from
# the pool of Labor Professions (like miner, lumberjack, farmer, etc).

def generate_Professions( Professions ):
    NPC_ProfessionType = Professions[random.randint(0, len(Professions) - 1)]
    #print(NPC_ProfessionType)

    NPC_SpecificProfession = 0
    if NPC_ProfessionType == "Labor_Professions":
        NPC_SpecificProfession = Labor_Professions[random.randint(0,len(Labor_Professions)-1)]
    if NPC_ProfessionType == "Combat_Professions":
        NPC_SpecificProfession = Combat_Professions[random.randint(0,len(Combat_Professions)-1)]
    if NPC_ProfessionType == "Service_Professions":
        NPC_SpecificProfession = Service_Professions[random.randint(0,len(Service_Professions)-1)]
    print("Profession -", NPC_SpecificProfession)

    return NPC_SpecificProfession

########################################################################################################################
# Chooses a random item from each list (Armor, weapons, backup weapon) and returns all the values.

def generate_Equipment(Armors, Weapons, Backup_Weapons):
    Armor = Armors[random.randint(0, len(Armors)-1)]
    print(Armor)
    Weapon = Weapons[random.randint(0, len(Weapons)-1)]
    print(Weapon)
    Backup_Weapon = Backup_Weapons[random.randint(0, len(Backup_Weapons)-1)]
    print(Backup_Weapon)

    return Armor, Weapon, Backup_Weapon

########################################################################################################################

#Main

print(" ")
print("NPC Generated:")
print(" ")
Race = generate_Race( Races )
print(" ")
#generate_Class( Classes )
Stats = generate_Stats(Stats, Race)
print(" ")
Profession = generate_Professions(Professions)
#generate_Equipment(Armors, Weapons, Backup_Weapons)