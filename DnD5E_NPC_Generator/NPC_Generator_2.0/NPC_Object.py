import random


class NPC:
    def __init__(self, race, age, sex, hair_style, facial_hair, hair_color, build, main_class, first_name, last_name, strength,
                 dexterity, constitution, intelligence, wisdom, charisma, strmod, dexmod, conmod, intmod, wismod, chamod,
                 weapon, armor, second_weapon, loot1, loot2, loot3 ):

        self.race = race
        self.age = age
        self.sex = sex
        self.hair_style = hair_style
        self.facial_hair = facial_hair
        self.hair_color = hair_color
        self.build = build
        self.main_class = main_class
        self.first_name = first_name
        self.last_name = last_name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.strmod = strmod
        self.dexmod = dexmod
        self.conmod = conmod
        self.intmod = intmod
        self.wismod = wismod
        self.chamod = chamod
        self.weapon = weapon
        self.armor = armor
        self.second_weapon = second_weapon
        self.loot1 = loot1
        self.loot2 = loot2
        self.loot3 = loot3

########################################################################################################################
# Opens file name passed to the program and reads in a random line

def random_Line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


########################################################################################################################
# Returns a random number from a designated range of values based on the Race passed to the function

def age_Generator(race):
    #print(race)
    if race == 'Elf' or race == 'Dwarf' or race == 'Dark-Elf' or race == 'High-Elf' or race == 'Wood-Elf' or race == 'Half-Elf':
        return random.randint(50, 750)
    if race == 'Gnome' or race == 'Halfling':
        return random.randint(50, 300)
    else:
        return random.randint(18, 55)

########################################################################################################################
# Simply picks Male or Female and returns them as a String

def sex_Generator():
    sexValue = random.randint(1,2)
    if sexValue == 1:
        return "Female"
    else:
        return "Male"

########################################################################################################################
# Rolls four die, identifies the lowest value, and then removes that lowest value from the total value of all the dice rolls
# combined. This number is returned. For example, If I roll 3, 4, 5, 6. This function drops the 3, and then would return
# 15.

def dice_Roll():
    rolls = [0,0,0,0]
    for i in range(len(rolls)):
        rolls[i] = ((random.randint(1,6)))
    #print(rolls)
    min_value = min(rolls)
    #print(min_value)
    roll_Total = 0
    for i in range(len(rolls)):
        roll_Total += rolls[i]
        #print(roll_Total)
    roll_Total -= min_value
    #print(roll_Total)
    return roll_Total

########################################################################################################################
# Receives a stat value and then returns the corresponding stat modifier that is paired with that value according to
# DnD 5e rules.

def stat_Modifier(stat):
    if stat == 1:
        return '-5'
    if stat >= 2 and stat <= 3:
        return '-4'
    if stat >= 4 and stat <= 5:
        return '-3'
    if stat >= 6 and stat <= 7:
        return '-2'
    if stat >= 8 and stat <= 9:
        return '-1'
    if stat >= 10 and stat <= 11:
        return '+0'
    if stat >= 12 and stat <= 13:
        return '+1'
    if stat >= 14 and stat <= 15:
        return '+2'
    if stat >= 16 and stat <= 17:
        return '+3'
    if stat >= 18 and stat <= 19:
        return '+4'

########################################################################################################################
########################################################################################################################

# Main #


race = random_Line('raceList.txt')
print("Race:", race)


age = age_Generator(race)
print("Age:", age)


sex = sex_Generator()
print("Gender:", sex)


# hair_Style is dependent on gender and pulls from separate .txt files
if sex == 'Male':
    hair_style = random_Line('MhairStyle_List.txt')
else:
    hair_style = random_Line('FhairStyle_List.txt')
print("Hair Style:", hair_style)


# facial_hair is dependent on the NPC being male
if sex == 'Male':
    facial_hair = random_Line('facialHair_List.txt')
    print("Facial Hair:", facial_hair)


hair_color = random_Line('hairColor_List.txt')
print("Hair Color:", hair_color)


# Body types / builds are dependent on gender and pull from different .txt files
if sex == 'Male':
    build = random_Line('Mbuild_List.txt')
else:
    build = random_Line('Fbuild_List.txt')
print("Body Type:", build)


main_class = random_Line('class_List.txt')
print("Character Class:", main_class)

########################################################################################################################
# ***In the future, make sure to create race AND gender based .txt files for first names. Last names only need to be
# dependent on race.

first_name = random_Line('Basic_FName_List.txt')
print("First Name:", first_name)

last_name = random_Line('Basic_LName_List.txt')
print("Last Name:", last_name)

########################################################################################################################

# Roll for basic stat values
strength = dice_Roll()
dexterity = dice_Roll()
constitution = dice_Roll()
intelligence = dice_Roll()
wisdom = dice_Roll()
charisma = dice_Roll()


# Adjust basic stat values based on racial perks
if race == 'Dwarf':
    constitution += 2

if race == 'Elf' or race == 'High-Elf' or race == 'Dark-Elf' or race == 'Wood-Elf' or race == 'Halfling':
    dexterity += 2

if race == 'Half-Orc':
    strength += 2
    constitution += 1

if race == 'Human':
    strength += 1
    dexterity += 1
    constitution += 1
    intelligence += 1
    wisdom += 1
    charisma += 1

if race == 'Gnome':
    intelligence += 2

# Half Elf is set to give Dex and Int as their two additional stats that get a boost. This needs to be changed to
# two random stats in the future
if race == 'Half-Elf':
    charisma += 2
    dexterity += 1
    intelligence += 1


# Determine stat modifiers based on basic stat values
strmod = stat_Modifier(strength)
dexmod = stat_Modifier(dexterity)
conmod = stat_Modifier(constitution)
intmod = stat_Modifier(intelligence)
wismod = stat_Modifier(wisdom)
chamod = stat_Modifier(charisma)

# Print all stats and their modifiers to screen
print("Strength:", strength, " ", strmod)
print("Dexterity:", dexterity, " ", dexmod)
print("Constitution:", constitution, " ", conmod)
print("Intelligence:", intelligence, " ", intmod)
print("Wisdom:", wisdom, " ", wismod)
print("Charisma:", charisma, " ", chamod)


weapon = random_Line('weapon_List.txt')
print("Weapon:", weapon)

armor = random_Line('armor_List.txt')
print("Armor:", armor)

second_weapon = random_Line('second_Weapon_List.txt')
print("Secondary Weapon: ", second_weapon)

