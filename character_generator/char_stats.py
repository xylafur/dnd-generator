
from lib.random_die import roll_d20, roll_d

STAT_TYPES = {'Strength': 0,
              'Constitution': 0,
              'Dexterity': 0,
              'Intelligence': 0,
              'Wisdom': 0,
              'Charisma': 0
              }

STANDARD_SCORES = [8, 10, 12, 13, 14, 15]

PROFICIENCY = {1: 2,
               2: 2,
               3: 2,
               4: 2,
               5: 3,
               6: 3,
               7: 3,
               8: 3,
               9: 4,
               10: 4,
               11: 4,
               12: 4,
               13: 5,
               14: 5,
               15: 5,
               16: 5,
               17: 6,
               18: 6,
               19: 6,
               20: 6
               }

def generate_stats_roll():
    """
        Generate stats based on d20 dice rolls.

        One extra roll is done, and the lowest is dropped.

        Returns:
             (:class: `dict`):  The stats with their scores.
    """
    gen_stats = []
    # Roll once extra for the number of stats to remove the lowest score later.
    for stat in range(0, len(STAT_TYPES.keys())+1):
        gen_stats.append(roll_d20(1))

    # Remove the lowest score.
    gen_stats.remove(min(gen_stats))

    i = 0
    stat_dict = {}
    for stat in STAT_TYPES:
        stat_dict[stat] = gen_stats[i]
        i += 1

    return stat_dict


def generate_stats_standard():
    """
        Generate stats based on the standard score array.

        Returns:
             (:class: `dict`):  The stats with their scores.
    """
    i = 0
    stat_dict = {}
    for stat in STAT_TYPES:
        stat_dict[stat] = STANDARD_SCORES[i]
        i += 1

    return stat_dict


def calculate_stat_mod(stats):
    """
        Generate modifier scores based on given stats.

        Args:
            stats (:class: `dict` or `int`):  The stats to calculate if a dict,
                or a single int to calculate if an integer.

        Returns:
             (:class: `dict` or `int`):  The stats with their modifiers, or an
                int single if an int was passed in.
    """
    stats_mod = {}

    if isinstance(stats, int):
        return int((stats / 2)) - 5

    for stat in stats:
        # Integer division so it truncates and takes the floor.
        # This is intentional.
        stats_mod[stat] = int((stats[stat] / 2)) - 5
    return stats_mod


def calculate_max_hp(stats, die, level):
    """
        Calculate the maximum hit points.

        Returns:
             (:class: `int`):  The maximum hp.
    """
    con_mod = calculate_stat_mod(stats)['Constitution']
    max_hp = die

    for lev in range(2, level):
        increase = roll_d(die) + con_mod

        # TODO: Not verifiable rule, but doing this to prevent negative hp values.
        if increase < 1:
            increase = 1
        max_hp += increase

    return max_hp


def calculate_base_ac(stats):
    """
        Calculate base AC without armor/spell modifiers.

        Returns:
             (:class: `int`):  The base AC minus equipment modifiers.
    """
    return calculate_stat_mod(stats)['Dexterity'] + 10


def get_proficiency_mod(level):
    """
        Gets the proficiency bonus for a specific level.

        Args:
            level (:class: `int`):  The level of the npc or character.

        Returns:
            (:class: `int`):  The proficiency bonus.
    """
    return PROFICIENCY[level]


def calculate_spell_dc(primary_stat, level):
    """
        Calculates the spell save DC for a given level and primary stat.

        Args:
            primary_stat (:class: `int`):  The stat value for calculating.

            level (:class: `int`):  The level of the npc or character.

        Returns:
            (:class: `int`):  The spell save DC.
    """
    stat = calculate_stat_mod(primary_stat)
    return 8 + get_proficiency_mod(level) + stat


def calculate_spell_attack_mod(primary_stat, level):
    """
       Calculates the spell attack modifier added to attack rolls.

       Args:
           primary_stat (:class: `int`):  The stat value for calculating.

           level (:class: `int`):  The level of the npc or character.

       Returns:
           (:class: `int`):  The spell attack modifier.
   """
    stat = calculate_stat_mod(primary_stat)
    return get_proficiency_mod(level) + stat
