# --- Day 7: The Treachery of Whales ---
# I am really sorry for what happened here.
# I had no idea how to solve it algorithmically, so i brute-forced it.
# I am deeply sorry for that.

def fuel_cost(vals: [int], pos: int) -> int:
    fuel = 0
    for v in vals:
        for i in range(1, int(abs(v - pos) + 1)):
            fuel += i
    return fuel


def find_smallest(vals: [int]) -> int:
    vals.sort()
    best_fc = 100000000000
    best_pos = 0
    for pos in range(vals[0], vals[len(vals) - 1]):
        fc = fuel_cost(vals, pos)
        print(f"{pos} : {fc}")
        if fc < best_fc:
            best_fc = fc
            best_pos = pos
    return best_pos


def main():
    crabs_positions = []

    with open("input.txt") as f:
        line = f.readline()
        for crab in line.split(","):
            crabs_positions.append(int(crab))

    final_position = 0
    print(crabs_positions)
    final_position = find_smallest(crabs_positions)
    print(f"Final position: {final_position}")
    print(f"Fuel cost: {fuel_cost(crabs_positions, final_position)}")


if __name__ == "__main__":
    main()
