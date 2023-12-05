"""This script solves Day 4 of Advent of Code 2023."""

FILE_PATH = "Day4/day4input.txt"
# FILE_PATH = "Day4/day4example.txt"


def get_card_value(card: str) -> int:
    """This function returns the value of one scratchcard.

    Args:
        card (str): The whole line read from the file, eg:
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'

    Returns:
        int: The value of the scratchcard.
    """
    # Get part after label, then separate into winning and own numbers.
    numbers = (card.split(":")[1]).split("|")
    # Split winning and own numbers into arrays
    winning_numbers = numbers[0].split()
    own_numbers = numbers[1].split()

    count_matches = 0
    # Count the number of matches
    for num in winning_numbers:
        if num in own_numbers:
            count_matches += 1

    # If no matches, the card is worth 0 points
    if count_matches == 0:
        return 0
    # Otherwise, the first match is worth 1 and then subsequent matches double
    # the card value. Since 2^0 = 1, this is exactly 2^[i-1]
    return 2 ** (count_matches - 1)


running_sum = 0
with open(FILE_PATH, "r") as file:
    for line in file:
        number = get_card_value(line)
        running_sum += number

print("Sum scratchcard values:", running_sum)
