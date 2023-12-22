"""This script solves Day 7 of Advent of Code 2023.

Part 1:
Find the rank of every hand in the set, and get the total winnings.

Some docstrings written with help of GitHub copilot.
"""

from typing import Dict, List
from collections import defaultdict

FILE_PATH = "Day7/input.txt"
# FILE_PATH = "Day7/example.txt"

face_card_value = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
# When we get the hand type during comparison, let's store it instead of recalculating
hand_type_hash: Dict[str, int] = {}


def calculate_hand_type(hand: str) -> int:
    """Calculates the type of a hand.

    Args:
        hand (str): The hand to determine the type of.

    Returns:
        int: The type of the hand.
            0: High card
            1: One pair
            2: Two pair
            3: Three of a kind
            4: Full house
            5: Four of a kind
            6: Five of a kind
    """

    counts_dict = defaultdict(int)
    # Get counts of each card
    for card in hand:
        counts_dict[card] += 1

    counts = sorted(counts_dict.values(), reverse=True)

    # Switch for types
    match len(counts):
        case 5:
            # High card
            return 0
        case 4:
            # One pair
            return 1
        case 1:
            # Five of a kind
            return 6

    match counts:
        case [2, 2, 1]:
            # Two pair
            return 2
        case [3, 1, 1]:
            # Three of a kind
            return 3
        case [3, 2]:
            # Full house
            return 4
        case [4, 1]:
            # Four of a kind
            return 5

    # If not an above type, throw an error
    raise ValueError(f"Hand with invalid type:{hand}")


def get_hand_type(hand: str) -> int:
    """
    Returns the hand type for the given hand.

    Args:
        hand (str): The hand to calculate the type for.

    Returns:
        int: The calculated hand type.
    """

    if hand not in hand_type_hash:
        hand_type_hash[hand] = calculate_hand_type(hand)
    return hand_type_hash[hand]


def is_hand_better(hand1: str, hand2: str) -> bool:
    """Determines if hand1 is better than hand2.

    Args:
        hand1 (str): First hand
        hand2 (str): Second hand

    Returns:
        bool: True if hand1 is better than hand2, False otherwise.
    """

    hand1_type = get_hand_type(hand1)
    hand2_type = get_hand_type(hand2)

    if hand1_type > hand2_type:
        return True
    if hand2_type > hand1_type:
        return False

    # equal types; compare cards
    for i in range(5):
        card1 = hand1[i]
        card2 = hand2[i]

        if card1 == card2:
            continue

        if card1.isdigit():
            card1 = int(card1)
        else:
            # isinstance(card1, str):
            card1 = face_card_value[card1]

        if card2.isdigit():
            card2 = int(card2)
        else:
            # isinstance(card2, str):
            card2 = face_card_value[card2]
        # if isinstance(card2, str):
        #     card2 = face_card_value[card2]

        # if card1.isdigit() and card2.isdigit():
        return card1 > card2
        # if isinstance(card1, str) and isinstance(card2, int):
        #     return True
        # if isinstance(card1, int) and isinstance(card2, str):
        #     return False
        # if isinstance(card1, str) and isinstance(card2, str):
        #     # There has to be a better way to do this....
        #     # Eliminate cards starting from high

        #     # Map letters to ints and just do >
        #     if card1 == "A":
        #         return True
        #     if card2 == "A":
        #         return False
        #     if card1 == "K":
        #         return True
        #     if card2 == "K":
        #         return False
        #     if card1 == "Q":
        #         return True
        #     if card2 == "Q":
        #         return False
        #     if card1 == "J":
        #         return True
        #     # Remaining card pair MUST be 1: T, 2: J
        #     # Can't both be T, and there's no other face cards
        #     return False


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merges two ranked lists of hands into one ranked list of hands.

    Args:
        left (List[int]): Left ranked list
        right (List[int]): Right ranked list

    Returns:
        List[int]: Merged ranked list, where the relative rank is the index + 1
    """
    # Psuedocode from geeksforgeeks.org/merge-sort/
    # Adapted from day 5

    li = 0  # Left pointer index
    ri = 0  # Right pointer index

    new_list = []
    while li < len(left) and ri < len(right):
        # Better hands get inserted later
        if not is_hand_better(left[li], right[ri]):
            # left worse than right
            new_list.append(left[li])
            li += 1
        else:
            # right worse than left
            new_list.append(right[ri])
            ri += 1

    # If there are any more items in right, merge items
    while ri < len(right):
        new_list.append(right[ri])
        ri += 1

    # If there are any more items in left, merge items
    while li < len(left):
        new_list.append(left[li])
        li += 1
    return new_list


def merge_sort_hands(hands: List[str]) -> List[str]:
    """Ranks a list of hands using merge sort.

    Args:
        hands (List[str]): List of hands to be ranked

    Returns:
        List[int]: Ranked list of hands, where the relative rank is the index + 1
    """
    # Adapted from day 5

    if len(hands) == 1:
        return hands

    mid = (len(hands)) // 2
    # Divide and conquer
    left = merge_sort_hands(hands[0:mid])
    right = merge_sort_hands(hands[mid : len(hands)])
    # Combine lists
    merged_hands = merge(left, right)

    return merged_hands


def parse_file_into_dict(
    file_path: str,
) -> Dict[str, int]:
    """Parses the input file into a dictionary mapping hands to their bets.

    Args:
        file_path (str): Path to input file

    Returns:
        Dict[str, int]: A dictionary mapping hands to their bets.
    """

    bets_dict: Dict[str, int] = {}
    # Get contents of file and store as table
    with open(file_path, "r") as file:
        for line in file:
            hand, bet = line.split()
            bets_dict[hand] = int(bet)

    return bets_dict


def get_total_winnings():
    """
    Calculates the total winnings based on the bets made on ranked hands.

    Returns:
        int: The total winnings.
    """
    bets_dict = parse_file_into_dict(FILE_PATH)

    ranked_hands = merge_sort_hands(list(bets_dict.keys()))

    running_sum = 0
    for i in range(len(ranked_hands)):
        running_sum += (i + 1) * bets_dict[ranked_hands[i]]

    return running_sum


print(get_total_winnings())
