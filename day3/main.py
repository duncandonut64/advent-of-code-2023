import os
input_file = open("day3-input.txt").read()
input_list = input_file.splitlines()
line_length = len(input_list[0])

print(line_length)

# Outline:
# Make a function to detect whether or not on an edge (one for each so LR TD)
# Figure out what length a number is based on the start and end indicies, then use for loop to skip
# Detect whether or not a number is adjacent to a non-period character
# Might be easier to split functions based off where to search for a character?
# For each number, check !(isdigit or is period) on all 8 adjacent tiles