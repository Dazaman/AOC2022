counter = 0

with open("input.txt") as file:
    lines = file.read().splitlines()
    
    for line in lines:
        l = line.split(",")[0]
        r = line.split(",")[1]

        left = list(range(int(l.split("-")[0]), int(l.split("-")[1])+1))
        right = list(range(int(r.split("-")[0]), int(r.split("-")[1])+1))

        ## PART1
        # if (set(left).issubset(right) or set(right).issubset(left)):
            # counter += 1
        
        if bool(set(left) & set(right)):
            counter+=1


    print(counter)