# https://adventofcode.com/2019/day/2#part2
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
intcode_list_path = os.path.join(my_path, "../day02/intcode_list.txt")

for noun in range(100):
    for verb in range(100):
        with open(intcode_list_path) as f:
            """
                1. Read the file
                2. Split it by commas into a list
                3. Map/Typecast every element of the list to an integer
                4. Make it into a list so we can use it
            """
            intcode_mass_list = list(map(int, f.read().split(",")))

            intcode_mass_list[1] = noun
            intcode_mass_list[2] = verb

            for i in range(0, len(intcode_mass_list), 4):
                if intcode_mass_list[i] == 1:
                    intcode_mass_list[intcode_mass_list[i + 3]] = \
                        intcode_mass_list[intcode_mass_list[i + 1]] + intcode_mass_list[intcode_mass_list[i + 2]]
                elif intcode_mass_list[i] == 2:
                    intcode_mass_list[intcode_mass_list[i + 3]] = \
                        intcode_mass_list[intcode_mass_list[i + 1]] * intcode_mass_list[intcode_mass_list[i + 2]]
                else:
                    break

                if intcode_mass_list[0] == 19690720:
                    print(f"To produce the output of 19690720, the noun has to be {noun} and "
                          f"the verb needs to be {verb}.")
                    exit()
