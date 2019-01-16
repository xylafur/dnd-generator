""" This is a module to generate a backstory based on xanthar's guide to everything """

import sys
sys.path.append("..")


from random import choice, randint

from scripts.namer import generate_name, choose_random_race
import scripts.stats

from utilities.races import races
from utilities.random_die import roll_event, roll_d100
from utilities.exceptions import RaceNotSupportedException
from utilities.random_die import roll_d4, roll_d6, roll_d8, roll_d10, \
                                   roll_d12, roll_d20, roll_d100



absent_parents = ["None", "Institution, such as an asylum", "Temple", 
                 "Orphanage", "guardian", "aunt", "uncle", "aunt and uncle", 
                 "grandparents", "adoptive family"]

#you were born in
birthplaces = [
     ((1, 50),"a home"), 
     ((51, 55), "the home of family friend"),
     ((56, 63),"the home of a {}".format(choice(["midwife", "healer"]))),
     ((64, 65),"a {}".format(choice(["carriage", "cart", "wagon"]))),
     ((66, 68),"a {}".format(choice(["barn", "shed", "outhouse"]))), 
     ((69, 70),"a cave"), 
     ((71, 72),"a field"), 
     ((73, 74),"a forest"),
     ((75, 77),"a temple"), 
     ((78, 78),"a battlefield"),
     ((79, 80),"a {}".format(choice(["street", "alley"]))),
     ((81, 82),"a {}".format(choice(["brothel", "tavern", "inn"]))),
     ((83, 84),"a {}".format(choice(["castle", "keep", "tower", "palace"]))),
     ((85, 85),"a sewer"),
     ((86, 88),"among people of a different race"),
     ((89, 91),"onboard a boat or a ship"),
     ((92, 93),"in a {}".format(choice(["prison", "headquarters of a secret organization"]))),
     ((94, 95),"in a sages lab"), ((96, 96),"in the feywild"),
     ((97, 97),"in the shadowfell"),
     ((98, 98),"in the {}".format(["Astral Plane", "Eterial Plane"])),
     ((99, 99),"in an inner plane of your choice"),
     ((100, 100),"in an outer plane of your choice")
    ]

#rthe number of siblings you had was
number_siblings = [
     ((1, 2), 0),
     ((3, 4), randint(1, 3)),
     ((5, 6), randint(1, 4) + 1),
     ((7, 8), randint(1, 6) + 2),
     ((9, 10), randint(1, 8) + 3),
    ]

#you were raised by
family = [
     ((1, 1), "no one, you had to raise yourself."),     
     ((2, 2), "an Institution, such as an asylum"),     
     ((3, 3), "individuals in a Temple"),     
     ((4, 5), "an Orphanage"),     
     ((6, 7), "a Guardian"),     
     ((8, 15), "a {}".format(choice(["aunt", "uncle", "aunt and uncle", "tribe", "clan"]))),     
     ((16, 25), "Grandparents"),     
     ((26, 35), "an Adoptive family"),     
     ((36, 55), "a Single father"),     
     ((56, 75), "a Single mother"),     
     ((76, 100), "both Mother and Father"),     
    ]

family_lifestyle = [
        ((3, 3), "Wretched"),
        ((4, 5), "Squalid"),
        ((6, 8), "Poor"),
        ((9, 12), "Modest"),
        ((13, 15), "Comfortable"),
        ((16, 17), "Wealthy"),
        ((18, 18), "Aristocratic"),
    ]

childhood_home_modifiers = {
    'Wretched': -40, 'Squalid': -20, 'Poor': -10, 'Modest': 0, 
    'Comfortable': 10, 'Wealthy': 20, 'Aristocratic': 40
}

#You grew up in
childhood_home = [
     ((-100, 0), "the streets"),
     ((1, 20), "a rundown shack"),
     ((21, 30), "no permenant residence, alot of moving"),
     ((31, 40), "a {}".format(choice(["Encampment", "Village in wilderness"]))),
     ((41, 50), "an Apartment in rundown neighborhood"),
     ((51, 70), "a Small House"),
     ((71, 90), "a Large House"),
     ((91, 110), "a Mansion"),
     ((111, 200), "a {}".format(choice(["Palace", "Castle"]))),
    ]

childhood_memories = [
     ((-100, 3), "still haunted by childhood"),
     ((4, 5), "spent most of childhood alone with no close friends"),
     ((6, 8), "Others saw me as being different or strange, and so I had few companions"),
     ((9, 12), "a few close friends and lived an ordinary childhood"),
     ((13, 15), "had several friends and childhood was generally a happy one"),
     ((16, 17), "always found it easy to make friends and loved being around people"),
     ((18, 100), "Everyone knew who I was, and had friends everywhere I went"),
    ]

parents = [((1, 95), "know parents"),
           ((95, 100), "don't know parents")]


cause_of_death = [
    "Unknown", "Murdered", "killed in battle", 
    "Accident related to occupation", "Accident unrelated to occupation", 
    "Old Age", "Disease", "Old Age", "Disease", "Apparent Suicide", "Torn apart by animal",
    "Consumed by monster", "Executed for crime", "Tortured to death", "Bizare event"
]

reason_absent = [
         ((1, 1), "parent died from {}".format(choice(cause_of_death))),
         ((2, 2), "parent was {}".format(choice(["imprisoned", "enslaved"]))),
         ((3, 3), "parent abandoned you"),
         ((4, 4), "parent disapeared to an unknown fate"),
    ]




def get_life_event():
    d100 = roll_d100(1)
    if d100 == 1:
        return "Weird event: " + weird_event()
    if d100 <= 10:
        return "Boons event: " + boons_event()
    if d100 <= 20:
        return "Love event: " + love_event()
    if d100 <= 30:
        return "Tragedy event: " + tragedy_event()
    if d100 <= 40:
        return "Enemy event: " + enemy_event()
    if d100 <= 50:
        return "Friend event: " + friend_event()
    if d100 <= 70:
        return "Job event: " + job_event()
    if d100 <= 75:
        return "Important Person event: " + important_person_event()
    if d100 <= 80:
        return "Adventure event: " + adventure_event()
    if d100 <= 85:
        return "Supernatural event: " + supernatural_event()
    if d100 <= 90:
        return "Battle event: " + battle_event()
    if d100 <= 95:
        return "Crime event: " + crime_event()
    return "Arcane event: " + arcane_event()


def get_life_events(age):
    """ returns a list of strings, each being a life event.
        The number of life events is based on the age of a person
    """
    def number_life_events(age):
        if age <= 20:
            return 1
        if age <= 30:
            return roll_d4(1)
        if age <= 40:
            return roll_d6(1)
        if age <= 50:
            return roll_d8(1)
        if age <= 60:
            return roll_d10(1)
        return roll_d12(1)
    events = []
    num_events = number_life_events(age)
    for _ in range(num_events):
        events.append(get_life_event())
    return events


def weird_event():
    events = [
        "You were turned into a toad for {} weeks".format(roll_d4(1)),
        "You were petrified and remained a strone statue for a time until someone freed you",
        "You were enslaved by a {} for {} years".format(choice(["hag", 
            "satyr", "troll"]), roll_d6(1)),
        "A dragon held you prisoner for {} months until adventurers killed it".format(roll_d4(1)),
        "You were taken captive by a group of {} and lived as a slave in the underdark".format(
            choice(["drow", "kuo-toa", "quaggoths"])),
        "You served a powerful adventurer as a hireling.",
        "You went insane for {} years and recently regained your sanity.".format(roll_d4(1)),
        "A lover of yours was secretly a silver dragon",
        "You were captuired by a cult and nearly sacrificed at the altar.  You escaped but fear they will find you",
        "You met a {} and lived to tell the tale".format(
            choice(["demigod", "archfey", "demon lord", "titan"])),
        "You were swallowed by a giant fish and spent a month in its gullet",
        "A powerful being granted you a wish, but you wasted it"
    ]
    return choice(events)


def love_event():
    gender = choice(["man", "woman"])

    gender = randint(0, 1)
    race = choice(races)
    name = generate_name(race, gender)

    return "You fell in love with a {} named {} {} years ago".format(gender,
        name, roll_d10(1))


def tragedy_event():
    events = [
    "A family member died from {}".format(choice(cause_of_death)),  
    "A friendship ended bitterly, and the person is now hostile towards you",
    "You lost all your possesions in a disaster and had to rebuild a new life",
    "You were imprisoned for a crome you didn't commit and spent {} years in hard labor".format(roll_d6(1)),
    "War ravaged your home community, reducing your hometown to rubble.  You {}".format(
        choice(["helped rebuild", "moved somewhere else"])),
    "A lover disapeared without a trace, you have been looking for them ever since",
    "A terrible blight in your community caused crops to fail and many starved, you lost a sibling",
    "You did something that brought terrible shame to your family",
    "For a reason you were never told, you were exiled from your home community and wandered the wilderness till you found a new home",
    "A romantic relationship ended on {} terms".format(choice(["good", "bad"])),
    "A {} romantic partner died from {}".format(choice(["current", "former"]), 
        choice(cause_of_death))
    ]
    return choice(events)


def enemy_event():
    dangerous = choice(["in danger", "not in danger"])
    blame = choice(["to blame", "not to blame"])

    gender = randint(0, 1)
    race = choice(races)
    name = generate_name(race, gender)

    event = "You made an enemy with {}, {} years ago.  You are {} for this.  Currently you are {}".format(
        name, roll_d4(1),  blame, dangerous)

    return event


def boons_event():
    events = [
        "A random wizard gave you a spell containing a cantrip",
        "You saved the life of a commoner who now owes you a life debt.  This individual accompanies you on your travels and performs mundane tasks for you.  He will leave if treated badly",
        "You found a horse",
        "You found {} gold".format(roll_d20(1)),
        "A relative gave you a simple weapon of your choice",
        "You found a trinket",
        "A friendly alchemist gifted you either a vial of healing potion or acid",
        "You found a treasure map", 
        "A distant relative dies and gives you enough money to life comfortable for {} years".format(roll_d20(1))
    ] 
    return choice(events)


def friend_event():
    """ Generate a random name and maybe some more details about this person
    """
    gender = randint(0, 1)
    race = choice(races)
    name = generate_name(race, gender)

    return "You made a friend earlier in life with {}".format(name)


def job_event():
    jobs = [
        "merchant", "guard", "alchemist", "hunter", "lute center employee", 
        "intern at IMM (International Magic Machines)", "Prostitute", 
        "barkeep", "musician", "farmer", "logger", "road maker", "carpenter", 
        "sailer", "fisherman"
    ]
    return "You used to work as a {}.  Start with 2 extra gold".format(choice(jobs))


def important_person_event():
    important_people = [
        "Yanther the Bloodthirsty"
    ]
    return "You met an important person named {}".format(choice(important_people))


def adventure_event():
    events = [
    "You nearly died.  You have nasty scars on your body and are missing {}".format(
        choice(["{} fingers".format(roll_d4(1)),
                       "{} toes".format(roll_d4(1))])),
    "You suffured a grievous injury,  Though it is healed it still pains you from time to time",
    "You were wounded, but in time you fully recovered",
    "You contracted a disease while exploring a filthy warren.  You recovered but have a persistent cough",
    "You were poisoned by a {} but survived".format(choice(["trap", "monster"])),
    "You lost something of sentimental value on a adventure",
    "You were terribly frightened by something you encountered and ran away, abandoning your companions to their fate",
    "You leared a great deal during your adventures.  Next time you make an ability check, roll with advantage",
    "You found some treasure on your adventure, you have {} left".format(
        roll_d12(1)),
    "You found a massive amount of treasure on your last adventure and still have {} gold".format(
        roll_d20(1) + 50),
    "You obtained a common magic item"

] 
    return choice(events)


def supernatural_event():
    events = [
        "You were ensorcelled by a fey and enslaved for {} years before you escaped".format(roll_d6(1)),
        "You saw a demon and ran away before it could do anything to you",
        "A devil tempted you. Make a DC 10 wisdom saving throw.  On a failed save, your allignment shifts 1 towards evil and you start the game with an aditional {} gold".format(
            roll_d20(1) + 50),
        "You woke up one morning miles from your home with no idea how you got there",
        "You visited a holy site and felt the presence of the divine there",
        "You witnessed {} and are convinced that it was an omen of some sort.".format(
            choice(["a falling red star", "a face apearing in the frost", "the queue", "a person apear from nowhere"])),
        "You escaped certain death and believe it was the intervention of a god that saved you",
        "You witnesed a minor miracle",
        "You explored an empty house and found it to be haunted",
        "You were briefly possesed by a {}".format(choice([
            "celestial", "devil", "demon", "fey", "elemental", "undead"])),
        "You saw a ghost", 
        "You saw a ghoul feeding on a corpse", 
        "A {} visited you in your dreams, warning you of danger to come".format(choice(["fiend", "celestial"])), 
        "You briefly visited the {}".format(choice(["Feywild", "Shadowfell"])),
        "You saw a portal that you believe leads to another plane of existance"
    ] 
    return choice(events)


def battle_event():
    events = [
        "You were knocked out and left for dead.  You woke up hours later with no recollection of battle",
        "YOu were badly injured in the fight, and you still bear awful scars",
        "You ran away from the battle to save your life, but you still feel the shame of you cowardice",
        "You suffered only minor injuries, and the wounds all healed without leaving any scars",
        "You survived the battle, but you suffer ptsd",
        "YOu escaped the battle unscathed, though many of your friends were injured or lost",
        "You proved yourself as a brave warrior in battle and received a medal as a sign of honor"
    ] 
    return choice(events)


def crime_event():
    crimes = ["murder", "theft", "burglary", "assult", "smuggling", "kidnapping",
              "extortion", "counterfeiting"]
    happened = ["were accused of", "commited"]
    caught = ["never caught", "caught and escaped", 
              "caught, were found guilty and went to jail", "caught and found not guilty"]

    return "You {} {} and {}".format(choice(happened), 
        choice(crimes), choice(caught))


def arcane_event():
    events = [
        "You were {} by a spell".format(choice(["charmed", "frightened"])),
        "You were injured by the effect of a spell",
        "You witnessed a powerful spell being cast by a {}".format(choice(
            ["wizard", "sorcerer", "warlock", "wizard"])),
        "You drank a potion of {}".format(choice(["love", "healing", "flatulince", "random death", "ungliness", "prettiness", "natural male enhancment"])),
        "You found a spell scroll and succeeded in casting the spell it contained",
        "You were affected by teleportation magic",
        "You turned invisable for a time",
        "You identified an illusion for what it was", 
        "You saw a creature being conjured by magic",
        "A fortune teller read your future and predicted: {}".format(get_life_event())
    ]
    return choice(events)

def generate_birthplace():
    return roll_event(100, birthplaces)

def generate_number_siblings():
    return roll_event(10, number_siblings)

def generate_who_raised():
    return roll_event(100, family)

def generate_reason_for_parent_absense():
    return roll_event(4, reason_absent)

def generate_childhood_socioeconomic_status():
    return roll_event(18, family_lifestyle, low=3)

def generate_childhood_home(modifier=None):
    if modifier == None: 
        return roll_event(200, childhood_home, low=-100)
    return roll_event(100, childhood_home, modifier=modifier)

def generate_childhood_memories(modifier=None):
    if modifier == None: 
        return roll_event(200, childhood_memories, low=-100)
    return roll_event(100, childhood_memories, modifier=modifier)

def generate_parents(race):
    mother = None
    father = None
    parents_names = [None, None]
    result = roll_event(100, parents)

    if "don't" in result:
        return result
    if 'half' in race:
        human_parent = choice([0, 1])
        parents_names[human_parent] = generate_name('human', human_parent)

        if 'orc' in race:
            parents_names[not human_parent] = generate_name('orc', not human_parent)
        elif 'dwarf' in race:
            parents_names[not human_parent] = generate_name('dwarf', not human_parent)
        else:
            raise RaceNotSupportedException(race)
    else:
        for ii in range(2):
            parents_names[ii] = generate_name(race, ii)
    return ("Knew parents, they were "+parents_names[0]+" and "+parents_names[1])

def generate_childhood(race, eco_class=None, birthplace=None, who_raised=None, 
                       num_sibs=None, home=None):
    """ Generates a childhood for an character, you may supply some of the 
        arguments, all of the arguments or none of the arguments.  For aruments
        not supplied, a random value will be generated
    """
    childhood = {}
    if not eco_class:
        childhood['class'] = generate_childhood_socioeconomic_status()
    else:
        childhood['class'] = eco_class

    if not birthplace:
        childhood['birthplace'] = generate_birthplace()
    else:
        childhood['birthplace'] = birthplace

    if not who_raised:
        childhood['who_raised'] = generate_who_raised()
    else:
        childhood['who_raised'] = who_raised
    
    if not num_sibs:
        childhood['num_sibs'] = generate_number_siblings()
    else:
        childhood['num_sibs'] = num_sibs

    childhood['parents absense'] = generate_reason_for_parent_absense() if \
            "Mother and Father" in childhood['who_raised'] else None
    childhood['parents'] = generate_parents(race)
    modifier = childhood_home_modifiers[childhood['class']]

    if not home:
        childhood['home'] = generate_childhood_home(modifier=modifier)
    else:
        childhood['home'] = home

    childhood['memories'] = generate_childhood_memories(modifier=modifier)

    return childhood


MALE = 1
FEMALE = 0

def generate_character_backstory(race=None, age=None, gender=None, name=None):
    gender_opt = 0
    if not gender:
        gender_opt = choice([MALE, FEMALE])
    if not race:
        race = choice(races)
    if not name:
        name = generate_name(race, gender_opt)
    if not age:
        age = randint(20, 100)
    
    #there is a personal decisions section that can be implemented later.. alot of work
    childhood = generate_childhood(race)
    life_events = get_life_events(age)

    return {
        'childhood': childhood, 'age': age, 'race': race, 'gender': gender, 
        'name': name, 'life_events': life_events
    }

CHARACTER = {}


def generate_character(*args, **kargs):
    """
        Generates a random npc with a backstory and stats.
    """
    # TODO: Do something with the arguments later.
    # TODO: This is admittedly awful.  This will be changed after we refine the libary.
    # It's currently here mostly for  testing purposes.
    gender = randint(0, 1)
    level = 4
    CHARACTER['Race'] = choose_random_race()
    CHARACTER['Gender'] = 'Male' if gender else 'Female'
    CHARACTER['Name'] = generate_name(CHARACTER['Race'], gender)
    CHARACTER['Background'] = generate_character_backstory()
    CHARACTER['Stats'] = stats.generate_stats_roll()
    CHARACTER['Stat Modifier'] = stats.calculate_stat_mod(CHARACTER['Stats'])
    CHARACTER['Base AC'] = stats.calculate_base_ac(CHARACTER['Stats'])
    # Intelligence is for the wizard class, just using as a test.
    CHARACTER['Spell Save DC'] = \
        stats.calculate_spell_dc(CHARACTER['Stats']['Intelligence'], level)
    CHARACTER['Spell Attack Mod'] = \
        stats.calculate_spell_attack_mod(CHARACTER['Stats']['Intelligence'],
                                         level)


    # TODO: To be better determined base on a class, for now hardcoding.
    CHARACTER['Maximum HP'] = stats.calculate_max_hp(CHARACTER['Stats'], 8,
                                                     level)
    for key in CHARACTER:
        # Generate and print all the stats.
        print("{}: {}".format(key, CHARACTER[key]))
