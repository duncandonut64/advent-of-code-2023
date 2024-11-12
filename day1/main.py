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

