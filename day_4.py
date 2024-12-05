with open("inputs/day_4_input.txt", "r") as f:
    data = f.readlines()

lines = [line.strip() for line in data]


##### Part 1 #####
def calc_possible_xmas(x_index, line_index):
    count = 0
    line = lines[line_index]

    # Check right
    if len(line) - x_index > 3 and line[x_index + 1] == "M":
        if line[x_index + 2] == "A":
            if line[x_index + 3] == "S":
                count += 1

    # Check left
    if x_index > 2 and line[x_index - 1] == "M":
        if line[x_index - 2] == "A":
            if line[x_index - 3] == "S":
                count += 1

    # Check up
    if line_index > 2 and lines[line_index - 1][x_index] == "M":
        if lines[line_index - 2][x_index] == "A":
            if lines[line_index - 3][x_index] == "S":
                count += 1

    # Check down
    if len(lines) - line_index > 3 and lines[line_index + 1][x_index] == "M":
        if lines[line_index + 2][x_index] == "A":
            if lines[line_index + 3][x_index] == "S":
                count += 1

    # Check right-down diagonal
    if (
        len(line) - x_index > 3
        and len(lines) - line_index > 3
        and lines[line_index + 1][x_index + 1] == "M"
    ):
        lines[line_index + 1][x_index + 1]
        if lines[line_index + 2][x_index + 2] == "A":
            if lines[line_index + 3][x_index + 3] == "S":
                count += 1

    # Check left-down diagonal
    if (
        x_index > 2
        and len(lines) - line_index > 3
        and lines[line_index + 1][x_index - 1] == "M"
    ):
        lines[line_index + 1][x_index - 1]
        if lines[line_index + 2][x_index - 2] == "A":
            if lines[line_index + 3][x_index - 3] == "S":
                count += 1

    # Check right-up diagonal
    if (
        len(line) - x_index > 3
        and line_index > 2
        and lines[line_index - 1][x_index + 1] == "M"
    ):
        lines[line_index - 1][x_index + 1]
        if lines[line_index - 2][x_index + 2] == "A":
            if lines[line_index - 3][x_index + 3] == "S":
                count += 1

    # Check left-up diagonal
    if x_index > 2 and line_index > 2 and lines[line_index - 1][x_index - 1] == "M":
        if lines[line_index - 2][x_index - 2] == "A":
            if lines[line_index - 3][x_index - 3] == "S":
                count += 1

    return count


xmas_count = 0
for idx, line in enumerate(lines):
    for jdx, ch in enumerate(line):
        if ch == "X":
            xmas_count += calc_possible_xmas(jdx, idx)

print(xmas_count)


##### Part 2 #####
def calc_possible_x_mas(x_index, line_index):
    line = lines[line_index]

    if (
        x_index < 1
        or line_index < 1
        or len(line) - x_index < 2
        or len(lines) - line_index < 2
    ):
        return 0

    # Check Right diaganol
    rb = lines[line_index + 1][x_index - 1]
    ru = lines[line_index - 1][x_index + 1]
    if rb not in ["M", "S"] or ru not in ["M", "S"] or rb == ru:
        return 0

    # Check Left diaganol
    lb = lines[line_index + 1][x_index + 1]
    lu = lines[line_index - 1][x_index - 1]
    if lb not in ["M", "S"] or lu not in ["M", "S"] or lb == lu:
        return 0

    return 1


x_mas_count = 0
for idx, line in enumerate(lines):
    for jdx, ch in enumerate(line):
        if ch == "A":
            x_mas_count += calc_possible_x_mas(jdx, idx)

print(x_mas_count)
