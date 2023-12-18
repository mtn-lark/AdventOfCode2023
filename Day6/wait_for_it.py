"""This script solves Day 6 of Advent of Code 2023.

Boat races! For a given race with n seconds, the time is split between charging
the boat's velocity (which gives 1 unit of distance per unit of time) and
moving based on the velocity charged (assume instant acceleration).
Part 1:
Find the number of ways to win races by beating the record.

Some docstrings written with help of GitHub copilot.
"""

from typing import List

FILE_PATH = "Day6/input.txt"
# FILE_PATH = "Day6/example.txt"


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

    count = 0

    # The distance traveled can be represented as x * (t - x),
    # where x is the time waited and t is the overall time.
    # So, this is a parabola maximized when x = t/2,
    # such that the distance traveled is (t/2)^2.
    t_max = time // 2
    print(t_max)

    if t_max * (time - t_max) > dist:
        count += 1
        for i in range(1, time - t_max):
            t_right = t_max + i
            t_left = t_max - i

            d_right = get_distance(t_right, time)
            d_left = get_distance(t_left, time)

            if not (d_left > dist or d_right > dist):
                # These charge times don't work, and since the function is
                # decreasing in the directions we're moving, we're not going
                # to find more solutions
                break

            if d_right > dist:
                count += 1
            if d_left > dist:
                count += 1
        return count
    else:
        # Even the highest value doesn't beat the record
        return count


# Set up variables
times: List[int] = []
distances: List[int] = []

# Parse file
file = open(FILE_PATH, "r")
times = [int(x) for x in (file.readline().split()[1::])]
distances = [int(x) for x in (file.readline().split()[1::])]
file.close()

running_product = 1
for i in range(len(times)):
    running_product *= get_num_ways_to_win(times[i], distances[i])

print(running_product)

# 31500 too low
