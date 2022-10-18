LOG_FILE="inputs/test2.log"

def read_log_file():
    log_entries = []
    with open(LOG_FILE, "r") as f:
        for line in f:
            if "eater_id" not in line:  # excluding header line
                log_line = tuple(line.strip().split())
                if log_line in log_entries:
                    raise Exception("duplicate entry")
                log_entries.append(log_line)
    return log_entries


def get_top_menu_items(log_entries):
    counts = {}
    for person_id, foodmenu_id in log_entries:
        counts[foodmenu_id] = counts.get(foodmenu_id, 0) + 1

    return sorted(counts.items(), key=lambda key: key[1])



if __name__ == "__main__":
    log_entries = read_log_file()
    top_counts = get_top_menu_items(log_entries)

    print("Top three foodmenu items are")
    print("foodmenu_id\tcounts")
    print("{}\t\t{}".format(top_counts[-1][0], top_counts[-1][1]))
    try:
        print("{}\t\t{}".format(top_counts[-2][0], top_counts[-2][1]))
    except KeyError:
        pass
    try:
        print("{}\t\t{}".format(top_counts[-3][0], top_counts[-3][1]))
    except KeyError:
        pass
