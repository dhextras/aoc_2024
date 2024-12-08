import os

with open("inputs/day_6_input.txt", "r") as f:
    data = f.readlines()

# Find the guard
guard_dir = 0  # 0 - up, 2 - down, 3 - left, 1 - right
guard_pos = (0, 0)  # line & pos
for idx, line in enumerate(data):
    if "^" in line:
        guard_pos = (idx, line.index("^"))
        break


# Just for the fun of it
def draw_map(lines):
    print("\033[H", end="")
    for line in lines:
        line = " ".join(list(line))
        print(line)


def draw_dir(dir):
    match dir:
        case 0:
            return "^"
        case 1:
            return ">"
        case 2:
            return "v"
        case 3:
            return "<"

    return "^"


######  Part 1  ######
moved_pos = set()
moved_pos.add(guard_pos)
lines = [list(line.strip()) for line in data]
drawable_lines = [line.strip() for line in data]


def get_next_pos(dir, pos, lines):
    line = lines[pos[0]]
    if (
        (dir == 0 and pos[0] < 1)
        or (dir == 2 and pos[0] + 1 == len(lines))
        or (dir == 3 and pos[1] < 1)
        or (dir == 1 and pos[1] + 1 == len(line))
    ):
        # Out of bounds
        return True, False, pos

    # Check the next one and return it if its not obst
    if dir == 0 and lines[pos[0] - 1][pos[1]] != "#":
        return False, False, (pos[0] - 1, pos[1])
    elif dir == 2 and lines[pos[0] + 1][pos[1]] != "#":
        return False, False, (pos[0] + 1, pos[1])
    elif dir == 3 and lines[pos[0]][pos[1] - 1] != "#":
        return False, False, (pos[0], pos[1] - 1)
    elif dir == 1 and lines[pos[0]][pos[1] + 1] != "#":
        return False, False, (pos[0], pos[1] + 1)

    return False, True, pos


os.system("clear")
while True:
    draw_map(drawable_lines)
    current_line = list(drawable_lines[guard_pos[0]])
    current_line[guard_pos[1]] = "X"
    drawable_lines[guard_pos[0]] = "".join(current_line)

    out_b, obst, guard_pos = get_next_pos(guard_dir, guard_pos, lines)
    moved_pos.add(guard_pos)

    current_line = list(drawable_lines[guard_pos[0]])
    current_line[guard_pos[1]] = draw_dir(guard_dir)
    drawable_lines[guard_pos[0]] = "".join(current_line)

    if out_b:
        break
    elif obst == True:
        if guard_dir == 3:
            guard_dir = 0
        else:
            guard_dir += 1

print(len(moved_pos))
