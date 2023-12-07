"""This script solves Day 5 of Advent of Code 2023.

Part 1:
Given seeds and a variety of mappings, this script prints the the lowest
location number that corresponds to any of the initial seeds.

Some docstrings written with help of GitHub copilot.
"""

from typing import List

# FILE_PATH = "Day5/input.txt"
FILE_PATH = "Day5/example.txt"


def merge_list(left: List[int], right: List[int]) -> List[int]:
    """Merges two sorted lists into one sorted list."""
    # Psuedocode from geeksforgeeks.org/merge-sort/

    li = 0  # Left pointer index
    ri = 0  # Right pointer index

    new_list = []
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            new_list.append(left[li])
            li += 1
        else:
            # right[ri] < left[li]
            new_list.append(right[ri])
            ri += 1

    # If there are any more items in left, merge items
    while li < len(left):
        new_list.append(left[li])
        li += 1

    # If there are any more items in right, merge items
    while ri < len(right):
        new_list.append(right[ri])
        ri += 1

    return new_list


def merge_sort_list(int_list: List[int]) -> List[int]:
    """Sorts a list of integers using merge sort.

    Args:
        int_list: List of integers to be sorted

    Returns:
        list
    """

    if len(int_list) == 1:
        return int_list

    mid = (len(int_list)) // 2
    # Divide and conquer
    left = merge_sort_list(int_list[0:mid])
    right = merge_sort_list(int_list[mid : len(int_list)])
    # Combine lists
    merge = merge_list(left, right)

    return merge
