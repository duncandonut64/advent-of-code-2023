import os
day1_input = open("day1-input.txt", "r")
day1_str = day1_input.read()
# print(day1_str)

list_digits = []

for line in day1_str.splitlines():
    for i in range(0, len(line)):
        if (line[i].isdigit()):
            firstDigit = line[i]
            break
    for i in range(0, len(line)):
        if (line[len(line) - 1 - i].isdigit()):
            lastDigit = line[len(line) - 1 - i]
            break
    list_digits.append((int) (firstDigit + lastDigit))

sum = 0
for i in list_digits:
    sum += i
print(sum) # Answer to question 1

num_dict = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

def parseStr(n):
    key_length = -1
    found_key = ""
    for key in num_dict.keys():
        if (n.count(key) != 0):
            key_length = len(key)
            found_key = key
            break
    if (key_length != -1):
        return num_dict.get(key)
    else:
        return -1

q2_list_digits = []

for line in day1_str.splitlines():
    for i in range(0, len(line)):
        lineStr = line[0:(i + 1)]
        if (line[i].isdigit()):
            firstDigit = line[i]
            break
        elif (parseStr(lineStr) != -1):
            firstDigit = parseStr(lineStr)
            break
    for i in range(0, len(line)):
        lineStr = line[(len(line) - i - 2):]
        if (line[len(line) - 1 - i].isdigit()):
            lastDigit = line[len(line) - 1 - i]
            break
        elif (parseStr(lineStr)!= -1):
            lastDigit = parseStr(lineStr)
            break
    # print(firstDigit)
    # print(lastDigit)
    # print(str(firstDigit) + str(lastDigit))
    q2_list_digits.append((int) (str(firstDigit) + str(lastDigit)))

q2_sum = 0
for i in q2_list_digits:
    q2_sum += i

print(q2_sum) # Answer to Question 2