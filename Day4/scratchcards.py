"""This script solves Day 4 of Advent of Code 2023."""

from typing import Dict
from collections import defaultdict

FILE_PATH = "Day4/day4input.txt"
# FILE_PATH = "Day4/day4example.txt"

scratchcard_counts: Dict[int, int] = defaultdict(int)


def get_number_matches(card: str) -> int:
    """This function returns the number of matches on one scratchcard.

    Args:
        card (str): The whole line read from the file, eg:
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'

    Returns:
        int: The number of matches on the scratchcard.
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

    return count_matches


def get_card_value(card: str) -> int:
    """This function returns the value of one scratchcard.

    Args:
        card (str): The whole line read from the file, eg:
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'

    Returns:
        int: The value of the scratchcard.
    """
    count_matches = get_number_matches(card)

    # If no matches, the card is worth 0 points
    if count_matches == 0:
        return 0
    # Otherwise, the first match is worth 1 and then subsequent matches double
    # the card value. Since 2^0 = 1, this is exactly 2^[i-1]
    return 2 ** (count_matches - 1)


def copy_scratchcards(card: str, card_number: int) -> None:
    """This function "copies" scratchcards by incrementing the global dictionary.

    Args:
        card (str): The whole line read from the file, eg:
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
        card_number (int): The number of the card.

    Returns: None
    """
    # Get number of matches
    count_matches = get_number_matches(card)

    # Get number of this card
    num_cards = scratchcard_counts[card_number]

    # Copy next i cards, once for each copy of this card
    for i in range(1, count_matches + 1):
        scratchcard_counts[card_number + i] += num_cards


point_sum = 0
card_number = 0
with open(FILE_PATH, "r") as file:
    for line in file:
        # Keep track of the card number
        card_number += 1

        # Part 1: Scratchcard points
        number = get_card_value(line)
        point_sum += number

        # Part 2: Scratchcard counts
        # Add the original card to the count of scratchcards
        scratchcard_counts[card_number] += 1
        copy_scratchcards(line, card_number)

print("Sum scratchcard values:", point_sum)
print("Total number scratchcards:", sum(scratchcard_counts.values()))
