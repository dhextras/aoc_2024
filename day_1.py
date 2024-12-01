##### Part 1 #####

with open("inputs/day_1_input.txt", "r") as f:
    data = f.readlines()

group1 = [line.split("   ")[0].strip() for line in data]
group2 = [line.split("   ")[1].strip() for line in data]

sorted_g1 = sorted(group1)
sorted_g2 = sorted(group2)

differences = 0
for i in range(len(data)):
    differences += abs(int(sorted_g1[i]) - int(sorted_g2[i]))

print(differences)


##### Part 1 #####
# TODO:
