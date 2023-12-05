from typing import Dict, List

FILE_PATH = "Day3/day3input.txt"
# FILE_PATH = "Day3/day3example.txt"

# File global vars
lines: List[str] = []
line_length: int = 0
num_lines: int = 0


def is_symbol(char: str) -> bool:
    if not char.isdigit() and char != "." and char != "\n":
        return True
    return False


def is_part(row_index: int, start_index: int, end_index: int) -> bool:
    number_string = lines[row_index][start_index : end_index + 1]
    # print(number_string)

    # Sanity check
    assert number_string.isdigit()

    # Check adjacent spots for symbol
    # This also checks the spots the number is in, but those will never read as
    # symbols.
    for r in range(row_index - 1, (row_index + 1) + 1):
        # Make sure row is valid
        if r >= 0 and r < num_lines:
            # Iterate through characters
            for i in range(start_index - 1, (end_index + 1) + 1):
                # Make sure index is valid
                if i >= 0 and i < line_length:
                    # Get character
                    char = lines[r][i]
                    if is_symbol(char):
                        return True

    # Symbol not found in scan
    return False


# Get contents of file and store as table
file = open(FILE_PATH, "r")
lines = file.readlines()
file.close()

# Store file information
line_length = len(lines[0])
num_lines = len(lines) - 1  # Empty line

running_sum: int = 0
row_index: int = 0
parts = set()
for line in lines:
    # Start/end indices are -1 if currently reading a non-digit.
    current_index: int = 0
    start_index: int = -1
    end_index: int = -1

    # Read numbers in line by reading each character
    for char in line:
        if char.isdigit():
            # If not reading number yet, note the start
            if start_index == -1:
                start_index = current_index
        else:
            # If reading number just finished
            if start_index != -1:
                end_index = current_index - 1
                # Check if we should add number to running sum
                if is_part(row_index, start_index, end_index):
                    number_string = lines[row_index][start_index : end_index + 1]
                    running_sum += int(number_string)
                    parts.add(int(number_string))
                start_index = -1
                end_index = -1

        # Increment index
        current_index += 1
    # Increment line index
    row_index += 1

print(running_sum)
