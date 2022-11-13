# --- Day 6: Lanternfish ---

def age_fishes(fishes_oga: []) -> []:
    new_fishes_oga = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # age all fishes (except for those aged 0)
    for i in range(1, 9):
        new_fishes_oga[i - 1] = fishes_oga[i]

    # fishes with age 0 reproduce and age
    new_fishes_oga[6] += fishes_oga[0]
    new_fishes_oga[8] += fishes_oga[0]

    return new_fishes_oga


def get_fish_count(fishes_oga: []) -> int:
    count = 0
    for age in fishes_oga:
        count += age
    return count


def main():
    fishes = []
    days = 80

    with open("input.txt") as f:
        line = f.readline()
        for fish in line.split(","):
            fishes.append(int(fish))

    # fishes of given age
    fishes_oga = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for fish in fishes:
        fishes_oga[fish] += 1

    for day in range(0, days):
        fishes_oga = age_fishes(fishes_oga)
        # print(fishes_oga)

    count = get_fish_count(fishes_oga)
    print(f"After {days} days of simulation, there are {count} fish")


if __name__ == "__main__":
    main()
