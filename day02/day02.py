# https://adventofcode.com/2019/day/2
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
intcode_list_path = os.path.join(my_path, "../day02/intcode_list.txt")

with open(intcode_list_path) as f:
    """
        1. Read the file
        2. Split it by commas into a list
        3. Map/Typecast every element of the list to an integer
        4. Make it into a list so we can use it
    """
    intcode_mass_list = list(map(int, f.read().split(",")))

    intcode_mass_list[1] = 12
    intcode_mass_list[2] = 2

    for i in range(0, len(intcode_mass_list), 4):
        if intcode_mass_list[i] == 1:
            intcode_mass_list[intcode_mass_list[i + 3]] = \
                intcode_mass_list[intcode_mass_list[i + 1]] + intcode_mass_list[intcode_mass_list[i + 2]]
        elif intcode_mass_list[i] == 2:
            intcode_mass_list[intcode_mass_list[i + 3]] = \
                intcode_mass_list[intcode_mass_list[i + 1]] * intcode_mass_list[intcode_mass_list[i + 2]]
        else:
            break

    print(intcode_mass_list[0])
