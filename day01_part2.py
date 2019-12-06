# https://adventofcode.com/2019/day/1#part2

total = 0
i = 0

input_mass_file = open("mass_list.txt", "r")

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
