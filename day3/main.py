import os
input_file = open("day3-input.txt").read()
input_list = input_file.splitlines()
line_length = len(input_list[0])

def checkCharacter(r, c):
    return not (input_list[r][c].isdigit() or input_list[r][c] == ".")

def checkBR(r, c):
    result = checkCharacter(r + 1, c)
    result = result or checkCharacter(r, c + 1)
    result = result or checkCharacter(r + 1, c + 1)
    return result

def checkBL(r, c):
    result = checkCharacter(r + 1, c)
    result = result or checkCharacter(r, c - 1)
    result = result or checkCharacter(r + 1, c - 1)
    return result

def checkTR(r, c):
    result = checkCharacter(r - 1, c)
    result = result or checkCharacter(r, c + 1)
    result = result or checkCharacter(r - 1, c + 1)
    return result

def checkTL(r, c):
    result = checkCharacter(r - 1, c)
    result = result or checkCharacter(r, c - 1)
    result = result or checkCharacter(r - 1, c - 1)
    return result

def checkR(r, c):
    result = checkCharacter(r + 1, c)
    result = result or checkCharacter(r - 1, c)
    result = result or checkCharacter(r - 1, c + 1)
    result = result or checkCharacter(r, c + 1)
    result = result or checkCharacter(r + 1, c + 1)
    return result

def checkL(r, c):
    result = checkCharacter(r + 1, c)
    result = result or checkCharacter(r - 1, c)
    result = result or checkCharacter(r - 1, c - 1)
    result = result or checkCharacter(r, c - 1)
    result = result or checkCharacter(r + 1, c - 1)
    return result

def checkT(r, c):
    result = checkCharacter(r, c - 1)
    result = result or checkCharacter(r - 1, c - 1)
    result = result or checkCharacter(r - 1, c)
    result = result or checkCharacter(r - 1, c + 1)
    result = result or checkCharacter(r, c + 1)
    return result

def checkB(r, c):
    result = checkCharacter(r, c - 1)
    result = result or checkCharacter(r + 1, c - 1)
    result = result or checkCharacter(r + 1, c)
    result = result or checkCharacter(r + 1, c + 1)
    result = result or checkCharacter(r, c + 1)
    return result

def checkAll(r, c):
    result = checkCharacter(r, c - 1)
    result = result or checkCharacter(r + 1, c - 1)
    result = result or checkCharacter(r + 1, c)
    result = result or checkCharacter(r + 1, c + 1)
    result = result or checkCharacter(r, c + 1)
    result = result or checkCharacter(r - 1, c + 1)
    result = result or checkCharacter(r - 1, c)
    result = result or checkCharacter(r - 1, c - 1)
    return result


print(input_list)





# Outline:
# Make a function to detect whether or not on an edge (one for each so LR TD)
# Figure out what length a number is based on the start and end indicies, then use for loop to skip
# Detect whether or not a number is adjacent to a non-period character
# Might be easier to split functions based off where to search for a character?
# For each number, check !(isdigit or is period) on all 8 adjacent tiles