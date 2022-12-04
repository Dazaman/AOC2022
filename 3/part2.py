badges = []

with open("input.txt") as file:
    while True:
        line1 = file.readline().strip()
        line2 = file.readline().strip()
        line3 = file.readline().strip()

        if not line2: break  # EOF

        common = list(set(line1) & set(line2) & set(line3))
        for i in common:
            badges.append(i)


total = sum([ord(char) - 96 if char.islower() else ord(char) - 38 for char in badges])
print(total)