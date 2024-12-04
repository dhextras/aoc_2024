import re

with open("inputs/day_3_input.txt", "r") as f:
    data = f.readlines()

data = "".join(data)
multiplier = lambda inp: sum(
    int(x) * int(y) for x, y in [mul.split(",") for mul in inp]
)

##### Part 1 #####
possible_muls = re.findall(r"mul\(([0-9,]+)\)", data)
print(multiplier(possible_muls))


##### Part 2 #####
dos = re.split(r"do\(\)", data)
print(
    sum(
        multiplier(do)
        for do in [
            re.findall(r"mul\(([0-9,]+)\)", dos)
            for dos in [re.split(r"don't\(\)", x)[0] for x in dos]
        ]
    )
)
