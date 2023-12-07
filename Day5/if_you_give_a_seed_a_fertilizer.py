"""This script solves Day 5 of Advent of Code 2023.

Part 1:
Given seeds and a variety of mappings, this script prints the the lowest
location number that corresponds to any of the initial seeds.

Some docstrings written with help of GitHub copilot.
"""

from typing import List, Tuple

# FILE_PATH = "Day5/input.txt"
FILE_PATH = "Day5/example.txt"


def merge_map(
    left: List[Tuple[int, int, int]], right: List[Tuple[int, int, int]]
) -> List[Tuple[int, int, int]]:
    """Merges two sorted maps (based on second item of tuple) into one sorted map.
    Maps are organized (destination range start, source range start, range length).

    Args:
        left (List[Tuple[int, int, int]]): Left sorted map
        right (List[Tuple[int, int, int]]): Right sorted map

    Returns:
        List[Tuple[int, int, int]]: Merged sorted map
    """

    li = 0  # Left pointer index
    ri = 0  # Right pointer index

    new_list = []
    while li < len(left) and ri < len(right):
        if left[li][1] <= right[ri][1]:
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


def merge_sort_map(map_list: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """Sorts a mapping list based on the second item of each tuple in the list.
    Maps are organized (destination range start, source range start, range length).


    Args:
        map_list (List[Tuple[int, int, int]]): List of mappings to be sorted

    Returns:
        List[Tuple[int, int, int]]: Sorted list of mappings
    """

    if len(map_list) == 1:
        return map_list

    mid = (len(map_list)) // 2
    # Divide and conquer
    left = merge_sort_map(map_list[0:mid])
    right = merge_sort_map(map_list[mid : len(map_list)])
    # Combine lists
    merge = merge_map(left, right)

    return merge


def merge_list(left: List[int], right: List[int]) -> List[int]:
    """Merges two sorted lists into one sorted list.

    Args:
        left (List[int]): Left sorted list
        right (List[int]): Right sorted list

    Returns:
        List[int]: Merged sorted list
    """
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
        int_list (List[int]): List of integers to be sorted

    Returns:
        List[int]: Sorted list of integers
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


def map_via_merge_sort(
    int_list: List[int], map_list: List[Tuple[int, int, int]]
) -> List[int]:
    """Maps a sorted list of integers using a sorted list of mappings.
    Maps are organized (destination range start, source range start, range length).

    Args:
        int_list (List[int]): Sorted list of integers
        map_list (List[Tuple[int, int, int]]): Sorted list of mappings

    Returns:
        List[int]: Mapped list of integers
    """

    i = 0  # int list pointer index
    m = 0  # map list pointer index

    new_list = []
    while i < len(int_list) and m < len(map_list):
        curr_int = int_list[i]
        curr_map = map_list[m]
        curr_map_source_range_start = curr_map[1]

        # Need to check if integer is in range for map, so if its above the map
        # source range start
        if curr_int < curr_map_source_range_start:
            # We know both lists are sorted. So, if the integer is smaller than
            # the next mapping, it must not be in a map.
            # Therefore, it maps to itself.
            new_list.append(curr_int)
            i += 1
        else:
            # if curr_int >= curr_map_source_range_start:
            curr_map_range_length = curr_map[2]
            curr_map_source_range_end = (
                curr_map_source_range_start + curr_map_range_length - 1
            )
            if curr_int <= curr_map_source_range_end:
                # Integer is in range!
                curr_map_dest_range_start = curr_map[0]
                difference = curr_map_dest_range_start - curr_map_source_range_start
                new_list.append(curr_int + difference)
                i += 1
            else:
                # Integer is bigger than this map, move on
                m += 1

    # If there are any more items in the int map, they are bigger than any map,
    # so they map to themselves. Add to the new list.
    while i < len(int_list):
        new_list.append(int_list[i])
        i += 1

    return new_list
