# pt 1

with open('day1/input.txt', 'r') as file:
    data = file.read().splitlines()

highest = 0
temp = 0

for line in data:
    if line == "":
        if temp > highest:
            highest = temp
        temp = 0
    else:
        temp += int(line)

print(highest)

# answer for my input: 72478