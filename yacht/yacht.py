# Score categories.
# Change the values as you see fit.
from itertools import count


YACHT = 'yacth'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

DICE_FACE = (1, 2, 3, 4, 5, 6)

def full_house_score(dice):
    counts_all = [dice.count(num) for num in DICE_FACE]
    counts = sorted(list(filter(lambda count: count > 0, counts_all)))

    if len(counts) == 2 and counts[0] == 2:
        return sum(dice)
    
    return 0


def four_of_a_dice_score(dice: list[int]):
    for num in DICE_FACE:
        if dice.count(num) >= 4:
            return 4 * num

    return 0


def score(dice, category):
    if category == YACHT:
        return 50 if sum(dice) / 5 == dice[0] else 0

    if 1 <= category <= 6:
        return sum(list(filter(lambda val: val == category, dice)))

    if category == FULL_HOUSE:
        return full_house_score(dice)
    
    if category == FOUR_OF_A_KIND:
        return four_of_a_dice_score(dice)
    
    if category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        return 0
    if category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        return 0
    if category == CHOICE:
        return sum(dice)
