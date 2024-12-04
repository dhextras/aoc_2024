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
# TODO: Do it for each A each check the 4 corners and check it only contains m s then check the proper mas
# by checking if the single diaganol is corners arent same
