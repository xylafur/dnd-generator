
from lib.random_die import roll_d20, roll_d

STAT_TYPES = {'Strength': 0,
              'Constitution': 0,
              'Dexterity': 0,
              'Intelligence': 0,
              'Wisdom': 0,
              'Charisma': 0
              }

STANDARD_SCORES = [8, 10, 12, 13, 14, 15]


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

        Returns:
             (:class: `dict`):  The stats with their modifiers.
    """
    stats_mod = {}

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


def calculate_base_AC(stats):
    """
        Calculate base AC without armor/spell modifiers.

        Returns:
             (:class: `int`):  The base AC minus equipment modifiers.
    """
    return calculate_stat_mod(stats)['Dexterity'] + 10
