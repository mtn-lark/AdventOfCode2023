FILE_PATH = "Day3/day3input.txt"
# FILE_PATH = "Day3/day3example.txt"

lines = []
line_length = 0
num_lines = 0


def is_part(row_index: int, start_index: int, end_index: int) -> bool:
    number_string = lines[row_index][start_index : end_index + 1]
    # print(number_string)

    # Sanity check
    assert number_string.isdigit()

    # Check adjacent spots for symbol
    # Top and bottom rows
    for r in range(row_index - 1, (row_index + 1) + 1, 2):
        # Make sure row is valid
        if r >= 0 and r < num_lines:
            # Iterate through characters
            for i in range(start_index - 1, (end_index + 1) + 1):
                # Make sure index is valid
                if i >= 0 and i < line_length:
                    # Get character
                    char = lines[r][i]
                    if not char.isdigit() and char != "." and char != "\n":
                        # Symbol found! Not digit or .
                        return True

    # Char to the left of number
    # Make sure it is in bounds
    if start_index - 1 >= 0:
        left_char = lines[row_index][start_index - 1]
        if not left_char.isdigit() and left_char != "." and left_char != "\n":
            # Symbol found! Not digit or .
            return True

    # Char to the right of number
    # Make sure it is in bounds
    if end_index + 1 < line_length:
        right_char = lines[row_index][end_index + 1]
        if not right_char.isdigit() and right_char != "." and right_char != "\n":
            # Symbol found! Not digit or .
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

running_sum = 0
row_index = 0
parts = set()
for line in lines:
    # Start/end indices are -1 if currently reading a non-digit.
    current_index = 0
    start_index = -1
    end_index = -1

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
