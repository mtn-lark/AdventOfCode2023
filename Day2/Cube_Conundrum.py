from typing import List

FILE_PATH = "Day2/day2input.txt"

running_sum = 0
game = 0


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
                raise (ValueError("Invalid color"))

    def __str__(self):
        return f"Red: {self.red}\nGreen: {self.green}\nBlue: {self.blue}"


class Game:
    # Class Variables
    trials: List[Trial] = []

    # Constructor method
    def __init__(self, game_raw_data) -> None:
        trials = []
        # Separate each trial
        trials_data = game_raw_data.split(";")
        for trial in trials_data:
            trials.append(Trial(trial))

        self.trials = trials


def check_possible_game():
    print("hello")


# Part 1
with open(file_path, "r") as file:
    for line in file:
        game += 1

        # First, separate the game from the data
        colon_index = line.find(":")
        game_raw_data = line[colon_index + 1 : -1]

        # Then, separate each trial
        trials = game_raw_data.split(";")
        print(trials)
        print(Trial(trial_raw_data=trials[0]))
        if game == 1:
            break
