# https://adventofcode.com/2019/day/4

start = 272091
end = 815432

possible_passwords = 0

for current_password in range(start, end+1):
    # turn the number into a string then into a list of integers so they can be compared
    b = [int(i) for i in str(current_password)]

    # loops through each number in the list then compares it to the next number and returns True if they are the same
    # checks if there are any Trues in the list every_check
    if any([b[i] == b[i+1] for i in range(len(b)-1)]):
        # checks that all are True to ensure the digits never decrease (e.g. this is bad 225576 but this is good 225579)
        if all([b[i] <= b[i + 1] for i in range(len(b) - 1)]):
            possible_passwords += 1

print(possible_passwords)
