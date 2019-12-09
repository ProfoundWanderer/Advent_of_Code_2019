# https://adventofcode.com/2019/day/1#part2
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
input_mass_path = os.path.join(my_path, "../day02/intcode_list.txt")

total = 0
i = 0

input_mass_file = open(input_mass_path, "r")

for i in input_mass_file:
    # convert the numbers from the files from str to int
    mass = int(i)
    while mass > 0:
        mass = ((mass//3)-2)
        # we want to stop when the mass is zero or negative
        if mass <= 0:
            break
        else:
            total += mass

print(total)
