from typing import List

FILE_PATH = "Day2/day2input.txt"

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


class Trial:
    # Class Variables
    red: int = 0
    green: int = 0
    blue: int = 0

    # Constructor method
    def __init__(self, trial_raw_data: str) -> None:
        # e.g. ' 12 blue, 15 red, 2 green'
        count_data = trial_raw_data.split(",")
        for count in count_data:
            color = (count.lstrip()).split()
            if color[1] == "red":
                self.red = int(color[0])
            elif color[1] == "green":
                self.green = int(color[0])
            elif color[1] == "blue":
                self.blue = int(color[0])
            else:
                raise (ValueError(f"Invalid color: {color[0]}"))

    def __str__(self) -> str:
        return f"Red: {self.red}\nGreen: {self.green}\nBlue: {self.blue}"


class Game:
    # Class Variables
    trials: List[Trial] = []
    _max_red_count = 0
    _max_green_count = 0
    _max_blue_count = 0

    # Constructor method
    def __init__(self, game_raw_data) -> None:
        trials = []
        max_red_count = 0
        max_green_count = 0
        max_blue_count = 0
        # Separate each trial
        trials_data = game_raw_data.split(";")
        for trial_datum in trials_data:
            trial = Trial(trial_datum)
            trials.append(trial)
            # Update maximum counts (for later validation)
            if trial.red > max_red_count:
                max_red_count = trial.red
            if trial.green > max_green_count:
                max_green_count = trial.green
            if trial.blue > max_blue_count:
                max_blue_count = trial.blue

        self.trials = trials
        self._max_red_count = max_red_count
        self._max_green_count = max_green_count
        self._max_blue_count = max_blue_count

    def __str__(self) -> str:
        trial_index = 0
        result = ""
        for trial in self.trials:
            result += f"* Trial {trial_index} *\n"
            result += str(trial) + "\n"
            trial_index += 1
        return result

    # Instance method
    def is_valid(self) -> bool:
        if self._max_red_count > MAX_RED:
            return False
        if self._max_green_count > MAX_GREEN:
            return False
        if self._max_blue_count > MAX_BLUE:
            return False
        return True

    def get_power(self) -> int:
        return self._max_red_count * self._max_green_count * self._max_blue_count


running_sum_part_1 = 0
running_sum_part_2 = 0
game = 0

# Part 1
with open(FILE_PATH, "r") as file:
    for line in file:
        game += 1

        # Separate the data
        colon_index = line.find(":")
        game_raw_data = line[colon_index + 1 : -1]

        game_data = Game(game_raw_data=game_raw_data)
        if game_data.is_valid():
            running_sum_part_1 += game
        running_sum_part_2 += game_data.get_power()

print(running_sum_part_1)
print(running_sum_part_2)
