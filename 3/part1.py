with open("input.txt") as file:
    lines = file.read().splitlines()

common = []

for l in lines:
    half = int(len(l)/2)
    firsthalf = l[:half]
    secondhalf = l[half:]

    commonchar = list(set(firsthalf) & set(secondhalf))
    
    for i in commonchar:
            common.append(i)

total = sum([ord(char) - 96 if char.islower() else ord(char) - 38 for char in common])
print(total)
