""" This is a module to generate a backstory based on xanthar's guide to everything """

import random

from lib.random_die import roll_d4, roll_d6, roll_d8, roll_d10, roll_d12, roll_d20, roll_d100
from info.races import races
from background_info.namer import generate_name


cause_of_death = [
    "Unknown", "Murdered", "killed in battle", 
    "Accident related to occupation", "Accident unrelated to occupation", 
    "Old Age", "Disease", "Old Age", "Disease", "Apparent Suicide", "Torn apart by animal",
    "Consumed by monster", "Executed for crime", "Tortured to death", "Bizare event"
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
    ret = ""
    for event in events:
        ret += '    ' + event + '\n'
    return ret 


def weird_event():
    events = [
        "You were turned into a toad for {} weeks".format(roll_d4(1)),
        "You were petrified and remained a strone statue for a time until someone freed you",
        "You were enslaved by a {} for {} years".format(random.choice(["hag", 
            "satyr", "troll"]), roll_d6(1)),
        "A dragon held you prisoner for {} months until adventurers killed it".format(roll_d4(1)),
        "You were taken captive by a group of {} and lived as a slave in the underdark".format(
            random.choice(["drow", "kuo-toa", "quaggoths"])),
        "You served a powerful adventurer as a hireling.",
        "You went insane for {} years and recently regained your sanity.".format(roll_d4(1)),
        "A lover of yours was secretly a silver dragon",
        "You were captuired by a cult and nearly sacrificed at the altar.  You escaped but fear they will find you",
        "You met a {} and lived to tell the tale".format(
            random.choice(["demigod", "archfey", "demon lord", "titan"])),
        "You were swallowed by a giant fish and spent a month in its gullet",
        "A powerful being granted you a wish, but you wasted it"
    ]
    return random.choice(events)


def love_event():
    gender = random.choice(["man", "woman"])

    gender = random.randint(0, 1)
    race = random.choice(races)
    name = generate_name(race, gender)

    return "You fell in love with a {} named {} {} years ago".format(gender,
        name, roll_d10(1))


def tragedy_event():
    events = [
    "A family member died from {}".format(random.choice(cause_of_death)),  
    "A friendship ended bitterly, and the person is now hostile towards you",
    "You lost all your possesions in a disaster and had to rebuild a new life",
    "You were imprisoned for a crome you didn't commit and spent {} years in hard labor".format(roll_d6(1)),
    "War ravaged your home community, reducing your hometown to rubble.  You {}".format(
        random.choice(["helped rebuild", "moved somewhere else"])),
    "A lover disapeared without a trace, you have been looking for them ever since",
    "A terrible blight in your community caused crops to fail and many starved, you lost a sibling",
    "You did something that brought terrible shame to your family",
    "For a reason you were never told, you were exiled from your home community and wandered the wilderness till you found a new home",
    "A romantic relationship ended on {} terms".format(random.choice(["good", "bad"])),
    "A {} romantic partner died from {}".format(random.choice(["current", "former"]), 
        random.choice(cause_of_death))
    ]
    return random.choice(events)


def enemy_event():
    dangerous = random.choice(["in danger", "not in danger"])
    blame = random.choice(["to blame", "not to blame"])

    gender = random.randint(0, 1)
    race = random.choice(races)
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
    return random.choice(events)


def friend_event():
    """ Generate a random name and maybe some more details about this person
    """
    gender = random.randint(0, 1)
    race = random.choice(races)
    name = generate_name(race, gender)

    return "You made a friend earlier in life with {}".format(name)


def job_event():
    jobs = [
        "merchant", "guard", "alchemist", "hunter", "lute center employee", 
        "intern at IMM (International Magic Machines)", "Prostitute", 
        "barkeep", "musician", "farmer", "logger", "road maker", "carpenter", 
        "sailer", "fisherman"
    ]
    return "You used to work as a {}.  Start with 2 extra gold".format(random.choice(jobs))


def important_person_event():
    important_people = [
        "Yanther the Bloodthirsty"
    ]
    return "You met an important person named {}".format(random.choice(important_people))


def adventure_event():
    events = [
    "You nearly died.  You have nasty scars on your body and are missing {}".format(
        random.choice(["{} fingers".format(roll_d4(1)),
                       "{} toes".format(roll_d4(1))])),
    "You suffured a grievous injury,  Though it is healed it still pains you from time to time",
    "You were wounded, but in time you fully recovered",
    "You contracted a disease while exploring a filthy warren.  You recovered but have a persistent cough",
    "You were poisoned by a {} but survived".format(random.choice(["trap", "monster"])),
    "You lost something of sentimental value on a adventure",
    "You were terribly frightened by something you encountered and ran away, abandoning your companions to their fate",
    "You leared a great deal during your adventures.  Next time you make an ability check, roll with advantage",
    "You found some treasure on your adventure, you have {} left".format(
        roll_d12(1)),
    "You found a massive amount of treasure on your last adventure and still have {} gold".format(
        roll_d20(1) + 50),
    "You obtained a common magic item"

] 
    return random.choice(events)


def supernatural_event():
    events = [
        "You were ensorcelled by a fey and enslaved for {} years before you escaped".format(roll_d6(1)),
        "You saw a demon and ran away before it could do anything to you",
        "A devil tempted you. Make a DC 10 wisdom saving throw.  On a failed save, your allignment shifts 1 towards evil and you start the game with an aditional {} gold".format(
            roll_d20(1) + 50),
        "You woke up one morning miles from your home with no idea how you got there",
        "You visited a holy site and felt the presence of the divine there",
        "You witnessed {} and are convinced that it was an omen of some sort.".format(
            random.choice(["a falling red star", "a face apearing in the frost", "the queue", "a person apear from nowhere"])),
        "You escaped certain death and believe it was the intervention of a god that saved you",
        "You witnesed a minor miracle",
        "You explored an empty house and found it to be haunted",
        "You were briefly possesed by a {}".format(random.choice([
            "celestial", "devil", "demon", "fey", "elemental", "undead"])),
        "You saw a ghost", 
        "You saw a ghoul feeding on a corpse", 
        "A {} visited you in your dreams, warning you of danger to come".format(random.choice(["fiend", "celestial"])), 
        "You briefly visited the {}".format(random.choice(["Feywild", "Shadowfell"])),
        "You saw a portal that you believe leads to another plane of existance"
    ] 
    return random.choice(events)


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
    return random.choice(events)


def crime_event():
    crimes = ["murder", "theft", "burglary", "assult", "smuggling", "kidnapping",
              "extortion", "counterfeiting"]
    happened = ["were accused of", "commited"]
    caught = ["never caught", "caught and escaped", 
              "caught, were found guilty and went to jail", "caught and found not guilty"]

    return "You {} {} and {}".format(random.choice(happened), 
        random.choice(crimes), random.choice(caught))


def arcane_event():
    events = [
        "You were {} by a spell".format(random.choice(["charmed", "frightened"])),
        "You were injured by the effect of a spell",
        "You witnessed a powerful spell being cast by a {}".format(random.choice(
            ["wizard", "sorcerer", "warlock", "wizard"])),
        "You drank a potion of {}".format(random.choice(["love", "healing", "flatulince", "random death", "ungliness", "prettiness", "natural male enhancment"])),
        "You found a spell scroll and succeeded in casting the spell it contained",
        "You were affected by teleportation magic",
        "You turned invisable for a time",
        "You identified an illusion for what it was", 
        "You saw a creature being conjured by magic",
        "A fortune teller read your future and predicted: {}".format(get_life_event())
    ]
    return random.choice(events)
