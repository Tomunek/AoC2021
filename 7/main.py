# --- Day 7: The Treachery of Whales ---

def med(vals: [int]) -> int:
    vals.sort()
    if len(vals) % 2:
        return vals[int(len(vals) / 2)]
    else:
        return (vals[int(len(vals) / 2)] + vals[int((len(vals) + 1) / 2)]) / 2


def fuel_cost(vals: [int], pos: int) -> int:
    fuel = 0
    for v in vals:
        fuel += abs(v - pos)
    return fuel


def main():
    crabs_positions = []

    with open("input.txt") as f:
        line = f.readline()
        for crab in line.split(","):
            crabs_positions.append(int(crab))

    final_position = 0
    print(crabs_positions)
    final_position = med(crabs_positions)
    print(f"Final position: {final_position}")
    print(f"Fuel cost: {fuel_cost(crabs_positions, final_position)}")


if __name__ == "__main__":
    main()
