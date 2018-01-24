from random import choice, randint

from background_info.backstory_generator import cause_of_death

absent_parents = ["None", "Institution, such as an asylum", "Temple", 
                 "Orphanage", "guardian", "aunt", "uncle", "aunt and uncle", 
                 "grandparents", "adoptive family"]

birthplaces = [
     ((1, 50),"Home"), ((51, 55), "Home of family friend"),
     ((56, 63),"Home of a {}".format(choice(["midwife", "healer"]))),
     ((64, 65),"{}".format(choice(["carriage", "cart", "wagon"]))),
     ((66, 68),"{}".format(choice(["barn", "shed", "outhouse"]))), 
     ((69, 70),"cave"), ((71, 72),"field"), ((73, 74),"forest"),
     ((75, 77),"temple"), ((78, 78),"battlefield"),
     ((79, 80),"{}".format(choice(["street", "alley"]))),
     ((81, 82),"{}".format(choice(["brothel", "tavern", "inn"]))),
     ((83, 84),"{}".format(choice(["castle", "keep", "tower", "palace"]))),
     ((85, 85),"sewer"),
     ((86, 88),"among people of a different race"),
     ((89, 91),"onboard a boat or a ship"),
     ((92, 93),"in a {}".format(choice(["prison", "headquarters of a secret organization"]))),
     ((94, 95),"in a sages lab"), ((96, 96),"in the feywild"),
     ((97, 97),"in the shadowfell"),
     ((98, 98),"in the {}".format(["Astral Plane", "Eterial Plane"])),
     ((99, 99),"in an inner plane of your choice"),
     ((100, 100),"in an outer plane of your choice")
    ]
number_siblings = [
     ((1, 2), 0),
     ((3, 4), randint(1, 3)),
     ((5, 6), randint(1, 4) + 1),
     ((7, 8), randint(1, 6) + 2),
     ((9, 10), randint(1, 8) + 3),
    ]

#this is actually more how you grew up, as far as how you were raised
family = [
     ((1, 1), "None"),     
     ((2, 2), "Institution, such as an asylum"),     
     ((3, 3), "Temple"),     
     ((4, 5), "Orphanage"),     
     ((6, 7), "Guardian"),     
     ((8, 15), "{}".format(choice(["aunt", "uncle", "aunt and uncle", "tribe", "clan"]))),     
     ((16, 25), "Grandparents"),     
     ((26, 35), "Adoptive family"),     
     ((36, 55), "Single father"),     
     ((56, 75), "Single mother"),     
     ((76, 100), "Mother and Father"),     
    ]
    
reason_absent = [
         ((1, 1), "Your parent died from {}".format(choice(cause_of_death))),
         ((2, 2), "Your parent was {}".format(choice(["imprisoned", "enslaved"]))),
         ((3, 3), "Your parent abandoned you"),
         ((4, 4), "Your parent disapeared to an unknown fate"),
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

childhood_home = [
     ((-100, 0), "On the streets"),
     ((1, 20), "Rundown Shack"),
     ((21, 30), "No permenant residence, alot of moving"),
     ((31, 40), "{}".format(choice(["Encampment", "Village in wilderness"]))),
     ((41, 50), "Apartment in rundown neighborhood"),
     ((51, 70), "Small House"),
     ((71, 90), "Large House"),
     ((91, 110), "Mansion"),
     ((111, 200), "{}".format(choice(["Palace", "Castle"]))),
    ]

childhood_memories = [
     ((-100, 3), "I am still haunted by my childhood"),
     ((4, 5), "I spent most of my childhood alone with no close friends"),
     ((6, 8), "Others saw me as being different or strange, and so I had few companions"),
     ((9, 12), "I had a few close friends and lived an ordinary childhood"),
     ((13, 15), "I had several friends and my chidhood was generally a happy one"),
     ((16, 17), "I always found it easy to make friends and Iloved being around people"),
     ((18, 100), "Everyone knew who I was, and I had friends everywhere I went"),
    ]

parents = [((1, 95), "You know who your parents are"),
           ((95, 100), "You don't know who your parents are")]

