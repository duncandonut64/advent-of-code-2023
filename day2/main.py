import os

input_file = open("day2-input.txt").read()
print(input_file)

def getRounds(input_str):
    round_list = input_str[input_str.index(":") + 2:].split(";")
    print(str(round_list))    
    return

def getCubes(input_str):
    return

for line in input_file.splitlines():
    # print(line)
    print(getRounds(line))