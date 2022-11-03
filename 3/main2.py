# --- Day 3: Binary Diagnostic ---
line_len = 12


def find_mask(lines: [str]) -> [int]:
    ones_counts = [0 for i in range(line_len)]
    for line in lines:
        for nbit in range(len(line) - 1):
            ones_counts[nbit] += int(line[nbit])
    return ones_counts


def remove_values(lines: [str], mask: str, bit: int) -> [str]:
    newlines = []
    for line in lines:
        if line[bit] == mask[bit]:
            newlines.append(line)
    return newlines


def find_value(lines: [str], select: int) -> str:
    line_count = len(lines)
    bit = 0
    while line_count > 1:
        ones_counts = find_mask(lines)
        mask = ""
        for i in ones_counts:
            if i >= line_count / 2:
                if select:
                    mask += "1"
                else:
                    mask += "0"
            else:
                if select:
                    mask += "0"
                else:
                    mask += "1"
        # print(mask)
        lines = remove_values(lines, mask, bit)
        # print(lines)
        bit += 1
        line_count = len(lines)
    return lines[0]


def main():
    oxygen_bin = ""
    co2_bin = ""
    oxygen = 0
    co2 = 0

    f = open("input.txt")
    lines = f.readlines()
    f.close()
    line_count = len(lines)

    oxygen_bin = find_value(lines, 1)
    co2_bin = find_value(lines, 0)

    print("Oxygen generator rating: " + str(oxygen_bin))
    print("CO2 scrubber rating: " + str(co2_bin))
    oxygen = int(oxygen_bin, 2)
    co2 = int(co2_bin, 2)
    print("Oxygen generator rating: " + str(oxygen))
    print("CO2 scrubber rating: " + str(co2))
    print("Product of gamma and epsilon rates (life support rating): " + str(oxygen * co2))


if __name__ == "__main__":
    main()
