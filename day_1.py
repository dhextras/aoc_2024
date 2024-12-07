with open("inputs/day_1_input.txt", "r") as f:
    data = f.readlines()

group1 = [line.split("   ")[0].strip() for line in data]
group2 = [line.split("   ")[1].strip() for line in data]

##### Part 1 #####
sorted_g1 = sorted(group1)
sorted_g2 = sorted(group2)

differences = 0
for i in range(len(data)):
    differences += abs(int(sorted_g1[i]) - int(sorted_g2[i]))

print(differences)


##### Part 2 #####
similarity_score = 0
sorted_g2_obj = {}

for i in group2:
    sorted_g2_obj[i] = sorted_g2_obj.get(i, 0) + 1

for j in group1:
    similarity_score += int(j) * sorted_g2_obj.get(j, 0)

print(similarity_score)
