file = open("input", "r")
report = file.readlines()
report = [i[:-1] for i in report]


def report_reducer(report_workshop: list, idx=0, most=True):
    no_0 = 0
    no_1 = 0
    report_reduced = []

    if len(report_workshop) == 1:
        return report_workshop
    else:

        for line in report_workshop:
            if line[idx] == "1":
                no_1 += 1
            else:
                no_0 += 1
        most_common = "1" if no_1 >= no_0 else "0"

        for line in report_workshop:
            if line[idx] == most_common and most is True:
                report_reduced.append(line)
            elif line[idx] != most_common and most is False:
                report_reduced.append(line)

    return report_reducer(report_reduced, idx + 1, most=most)


ox_gen_rat_raw = report_reducer(report)
ox_gen_rat = int(ox_gen_rat_raw[0], 2)
co2_scr_rat_raw = report_reducer(report, most=False)
co2_scr_rat = int(co2_scr_rat_raw[0], 2)

life_support_rating = ox_gen_rat * co2_scr_rat

print(f"Life support: {life_support_rating}")
