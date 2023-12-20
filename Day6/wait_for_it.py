"""This script solves Day 6 of Advent of Code 2023.

Boat races! For a given race with n seconds, the time is split between charging
the boat's velocity (which gives 1 unit of distance per unit of time) and
moving based on the velocity charged (assume instant acceleration).
Part 1:
Find the number of ways to win each of the races by beating the record.
Part 2:
Kerning is off! It's just one race. Find the number of ways to win by beating
the record.

Some docstrings written with help of GitHub copilot.
"""

from typing import List, Tuple
from math import sqrt, floor

FILE_PATH = "Day6/input.txt"
# FILE_PATH = "Day6/example.txt"


def solve_quadratic(a: int, b: int, c: int) -> Tuple[float, float] | None:
    """
    Solve a quadratic equation of the form ax^2 + bx + c = 0.

    Args:
        a (int): Coefficient of x^2.
        b (int): Coefficient of x.
        c (int): Constant term.

    Returns:
        Tuple[float, float]: The two solutions of the quadratic equation.
    """
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None

    solution1 = (-b + sqrt(discriminant)) / (2 * a)
    solution2 = (-b - sqrt(discriminant)) / (2 * a)

    return (solution1, solution2)


def get_distance(time_waited: int, time_total: int) -> int:
    """
    Calculates the distance traveled based on the time waited and the total time.

    Args:
        time_waited (int): The time waited before starting movement.
        time_total (int): The total time of the race.

    Returns:
        int: The distance traveled.
    """
    return time_waited * (time_total - time_waited)


def get_num_ways_to_win(time: int, dist: int) -> int:
    """
    Calculate the number of ways to win based on the given time and distance.

    Args:
        time (int): The time available to reach the destination.
        dist (int): The distance to be covered.

    Returns:
        int: The number of ways to win.
    """

    # The distance traveled can be represented as x * (t - x) = -x^2 + tx,
    # where x is the time waited and t is the overall time.
    # We can subtract the record distance d to get -x^2 + tx - d.
    # This is a quadratic where the solutions represent the amount of time
    # needed to charge to match the record distance; so, the number of ways to
    # win is the number of integers between those two solutions.

    solution = solve_quadratic(-1, time, -dist)
    if not solution:
        return 0

    sol1, sol2 = solution
    # if sol1 < sol2, the number of ints between the solutions would be
    # floor(sol2) - ciel(sol1), +1 to include the upper bound.
    # However, we can just floor both and take the absolute value to avoid
    # comparing and automatically include the bounds.
    return abs(floor(sol1) - floor(sol2))


# Set up variables
times: List[int] = []
distances: List[int] = []


def get_part_1():
    # Parse file
    file = open(FILE_PATH, "r")
    times = [int(x) for x in (file.readline().split()[1::])]
    distances = [int(x) for x in (file.readline().split()[1::])]
    file.close()

    running_product = 1
    for i in range(len(times)):
        running_product *= get_num_ways_to_win(times[i], distances[i])

    print("Part 1:", running_product)


def get_part_2():
    # Parse file
    file = open(FILE_PATH, "r")
    # Kerning is bad! It's just one number!
    # Get everything after the colon, replace all the spaces with empty, and
    # cast to int.
    time = int(file.readline().split(":")[1].replace(" ", ""))
    dist = int(file.readline().split(":")[1].replace(" ", ""))

    print("Part 2:", get_num_ways_to_win(time, dist))


get_part_1()
get_part_2()
