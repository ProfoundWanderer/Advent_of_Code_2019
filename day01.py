# https://adventofcode.com/2019/day/1

total = 0

input_mass_file = open("mass_list.txt", "r")

for i in input_mass_file:
    # convert the numbers from the files from str to int
    mass = int(i)
    total += ((mass//3)-2)

print(total)
