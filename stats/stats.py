
from lib.random_die import roll_d20

STAT_TYPES = {'strength': 0,
              'constitution': 0,
              'dexterity': 0,
              'intelligence': 0,
              'wisdom': 0,
              'charisma': 0
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
    for stat in STAT_TYPES:
        STAT_TYPES[stat] = gen_stats[i]
        i += 1

    return STAT_TYPES


def generate_stats_standard():
    """
        Generate stats based on the standard score array.

        Returns:
             (:class: `dict`):  The stats with their scores.
    """
    i = 0
    for stat in STAT_TYPES:
        STAT_TYPES[stat] = STANDARD_SCORES[i]
        i += 1

    return STAT_TYPES
