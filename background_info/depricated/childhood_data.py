from random import choice, randint

from background_info.depricated.backstory_generator import cause_of_death

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

reason_absent = [
         ((1, 1), "parent died from {}".format(choice(cause_of_death))),
         ((2, 2), "parent was {}".format(choice(["imprisoned", "enslaved"]))),
         ((3, 3), "parent abandoned you"),
         ((4, 4), "parent disapeared to an unknown fate"),
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
     ((-100, 3), "still haunted by depricated.childhood"),
     ((4, 5), "spent most of depricated.childhood alone with no close friends"),
     ((6, 8), "Others saw me as being different or strange, and so I had few companions"),
     ((9, 12), "a few close friends and lived an ordinary depricated.childhood"),
     ((13, 15), "had several friends and depricated.childhood was generally a happy one"),
     ((16, 17), "always found it easy to make friends and loved being around people"),
     ((18, 100), "Everyone knew who I was, and had friends everywhere I went"),
    ]

parents = [((1, 95), "know parents"),
           ((95, 100), "don't know parents")]

