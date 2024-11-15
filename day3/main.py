import os
# input_file = open("test.txt").read()
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

def check(r, c):
    result = False
    if (r == 0 and c == 0):
        result = result or checkBR(r, c)
    elif (r == 0 and c == line_length - 1):
        result = result or checkBL(r, c)
    elif (r == line_length - 1 and c == 0):
        result = result or checkTR(r, c)
    elif (r == line_length - 1 and c == line_length - 1):
        result = result or checkTL(r, c)
    elif (r == 0):
        result = result or checkB(r, c)
    elif (r == line_length - 1):
        result = result or checkT(r, c)
    elif (c == 0):
        result = result or checkR(r, c)
    elif (c == line_length - 1):
        result = result or checkL(r, c)
    else:
        result = result or checkAll(r, c)
    return result

def checkNumber(r, c):
    current_str = input_list[r][c]
    result = check(r, c)
    current_index = c
    if (current_index < line_length - 1):
        current_index = c + 1
        nextDigit = input_list[r][current_index]
        while (nextDigit.isdigit() and (current_index < line_length - 1)):
            print("Next Digit:")
            print(nextDigit)
            current_str = current_str + str(nextDigit)
            # print(current_index)
            result = result or check(r, current_index)
            current_index += 1
            nextDigit = input_list[r][current_index]
        if (current_index == line_length - 1):
            result = result or check(r, current_index)
            nextDigit = input_list[r][current_index]
            if (nextDigit.isdigit()):
                current_str = current_str + str(nextDigit)
    return current_str, result, current_index
# def checkNumber(r, c):
#     current_str = input_list[r][c]
#     result = check(r, c)
#     current_index = c
#     if (current_index < line_length - 1):
#         current_index = c + 1
#         nextDigit = input_list[r][current_index]
#         while (nextDigit.isdigit() and (current_index < line_length - 1)):
#             print("Next Digit:")
#             print(nextDigit)
#             current_str = current_str + str(nextDigit)
#             # print(current_index)
#             result = result or check(r, current_index)
#             current_index += 1
#             nextDigit = input_list[r][current_index]
#     return current_str, result, current_index - c

sum = 0
for r in range(0, line_length):
    c = 0
    while (c < line_length):
        if (input_list[r][c].isdigit()):
            num_str, counted, skip = checkNumber(r, c)
            if (counted):
                print("Found " + str(num_str) + " at (" + str(r) + ", " + str(c) + ")")
                sum += int(num_str)
                c = skip
                # if (c + skip > line_length):
                #     c = line_length
                # else:
                #     c += skip + 1
            else:
                c += 1
        else:
            c += 1

# print(input_list)
print(sum)





# Outline:
# Make a function to detect whether or not on an edge (one for each so LR TD)
# Figure out what length a number is based on the start and end indicies, then use for loop to skip
# Detect whether or not a number is adjacent to a non-period character
# Might be easier to split functions based off where to search for a character?
# For each number, check !(isdigit or is period) on all 8 adjacent tiles