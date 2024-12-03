with open("inputs/day_2_input.txt", "r") as f:
    data = f.readlines()

reports = [[int(i) for i in line.strip().split(" ")] for line in data]


def is_safe_report(report):
    start_pattern = None
    safe = True

    for i in range(len(report) - 1):
        current_level = report[i]
        next_level = report[i + 1]
        diff = abs(current_level - next_level)

        pattern = 1 if current_level > next_level else 0  # 1 - decr, 0 - incr
        if start_pattern is None:
            start_pattern = pattern

        if (diff <= 0 or diff > 3) or start_pattern != pattern:
            safe = False
            break

    return safe


##### Part 1 #####
safe_count = 0
for report in reports:
    if is_safe_report(report):
        safe_count += 1

print(safe_count)


##### Part 2 #####

# Remove the single bad level & and a bad report
safe_count2 = 0
for report in reports:
    if is_safe_report(report):
        safe_count2 += 1
        continue

    for i in range(len(report)):
        temp_report = report.copy()
        temp_report.pop(i)

        if is_safe_report(temp_report):
            safe_count2 += 1
            break

print(safe_count2)
