with open("inputs/day_5_input.txt", "r") as f:
    data = f.readlines()

rules = []
updates = []

for line in data:
    if "|" in line:
        rules.append(line.strip())
    elif "," in line:
        updates.append(line.strip())

##### Part 1 #####
middle_total = 0
for update in updates:
    failed_rule = False
    update = update.split(",")

    for rule in rules:
        try:
            rule = rule.split("|")
            f_rule = update.index(rule[0])
            l_rule = update.index(rule[1])
            if f_rule > l_rule:
                failed_rule = True

        except ValueError:
            pass

    if not failed_rule:
        middle_total += int(update[int((len(update) - 1) / 2)])

print(middle_total)

##### Part 2 #####
failed_updates = []
corrected_middle_total = 0

for update in updates:
    update = update.split(",")

    def correct_update(update):
        failed_rule = False
        for rule in rules:
            try:
                rule = rule.split("|")

                uf_rule = update.index(rule[0])
                ul_rule = update.index(rule[1])

                if uf_rule > ul_rule:
                    failed_rule = True
                    ofv_rule = update[ul_rule]
                    olv_rule = update[uf_rule]
                    update[uf_rule] = ofv_rule
                    update[ul_rule] = olv_rule

                    update, _ = correct_update(update)

            except ValueError:
                pass

        return update, failed_rule

    corrected_update, failed_rule = correct_update(update)

    if failed_rule:
        corrected_middle_total += int(
            corrected_update[int((len(corrected_update) - 1) / 2)]
        )

print(corrected_middle_total)
