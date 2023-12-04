file_path = "day1input.txt"

running_sum = 0

# Part 1
"""
with open(file_path, "r") as file:
    for line in file:
        number = 0
        # read from right
        for char in line:
            if char.isdigit():
                number += 10 * int(char)
                break
        # read from left
        for char in reversed(line):
            if char.isdigit():
                number += int(char)
                break
        # add number to running sum
        running_sum += number
"""

# Part 2
digit_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open(file_path, "r") as file:
    for line in file:
        number = 0
        # read from right
        for char in line:
            if char.isdigit():
                number += 10 * int(char)
                break
        # read from left
        for char in reversed(line):
            if char.isdigit():
                number += int(char)
                break
        # add number to running sum
        running_sum += number

print(running_sum)
