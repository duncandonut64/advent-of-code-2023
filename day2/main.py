import os

input_file = open("day2-input.txt").read()
# print(input_file)

def getRounds(input_str):
    round_list = input_str[input_str.index(":") + 2:].split(";")
    # print(str(round_list))    
    return round_list

def getGameID(input_str):
    id_str = input_str.split(" ")[1]
    return int(id_str[0:(len(id_str) - 1)])

def getCubes(round):
    rgb = [0, 0, 0]
    parsedRound = round.replace(",", "").split(" ")
    print(parsedRound)
    if (parsedRound.count("red") != 0):
        rgb[0] = int(parsedRound[parsedRound.index("red") - 1])
    if (parsedRound.count("green") != 0):
        rgb[1] = int(parsedRound[parsedRound.index("green") - 1])
    if (parsedRound.count("blue") != 0):
        rgb[2] = int(parsedRound[parsedRound.index("blue") - 1])
    return rgb

def gamePossible(cubes):
    return cubes[0] <= 12 and cubes[1] <= 13 and cubes[2] <= 14

def maxCubes(game):
    rounds = getRounds(game)
    print("Game Number: " + str(getGameID(game)))
    max_rgb = [0, 0, 0]
    for round in rounds:
        round_rgb = getCubes(round)
        print("Current round: ")
        print(round_rgb)
        if (round_rgb[0] > max_rgb[0]):
            print("Old max: " + str(max_rgb[0]))
            print("New max: " + str(round_rgb[0]))
            max_rgb[0] = round_rgb[0]
        if (round_rgb[1] > max_rgb[1]):
            max_rgb[1] = round_rgb[1]
        if (round_rgb[2] > max_rgb[2]):
            max_rgb[2] = round_rgb[2]
    print(max_rgb)
    if gamePossible(max_rgb):
        return getGameID(game)
    else:
        # print(game)
        # print(max_rgb)
        return 0

def getPower(game):
    rounds = getRounds(game)
    print("Game Number: " + str(getGameID(game)))
    max_rgb = [0, 0, 0]
    for round in rounds:
        round_rgb = getCubes(round)
        print("Current round: ")
        print(round_rgb)
        if (round_rgb[0] > max_rgb[0]):
            print("Old max: " + str(max_rgb[0]))
            print("New max: " + str(round_rgb[0]))
            max_rgb[0] = round_rgb[0]
        if (round_rgb[1] > max_rgb[1]):
            max_rgb[1] = round_rgb[1]
        if (round_rgb[2] > max_rgb[2]):
            max_rgb[2] = round_rgb[2]
    return max_rgb[0] * max_rgb[1] * max_rgb[2]

sum = 0
for line in input_file.splitlines():
    # sum += maxCubes(line) # Question 1 
    sum += getPower(line) # Question 2 

print(sum)