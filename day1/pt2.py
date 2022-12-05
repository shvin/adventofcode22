# pt 2

with open('day1/input.txt', 'r') as file:
    data = file.read().splitlines()

highest1 = 0
highest2 = 0
highest3 = 0
temp = 0

for line in data:
    if line == "":
        if temp > highest3:
            if temp > highest2:
                if temp > highest1:
                    highest3 = highest2
                    highest2 = highest1
                    highest1 = temp
                else:
                    highest3 = highest2
                    highest2 = temp
            else:
                highest3 = temp
        temp = 0
    else:
        temp += int(line)
        
print(highest1)
print(highest2)
print(highest3)
print(highest1 + highest2 + highest3)

# answer for my input: 210367