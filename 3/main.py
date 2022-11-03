# --- Day 3: Binary Diagnostic ---

def main():
    ones_counts = [0 for i in range(12)]
    gamma_bin = ""
    epsilon_bin = ""
    gamma = 0
    epsilon = 0
    line_count = 0
    with open("input.txt") as f:
        lines = f.readlines()
        line_count = len(lines)
        for line in lines:
            for nbit in range(len(line) - 1):
                ones_counts[nbit] += int(line[nbit])

    for i in ones_counts:
        if i > line_count / 2:
            gamma_bin += "1"
            epsilon_bin += "0"
        else:
            gamma_bin += "0"
            epsilon_bin += "1"

    print("Lines: " + str(line_count))
    print("1's counted: ")
    print(ones_counts)
    print("Gamma rate: " + str(gamma_bin))
    print("Epsilon rate: " + str(epsilon_bin))
    gamma = int(gamma_bin, 2)
    epsilon = int(epsilon_bin, 2)
    print("Gamma rate: " + str(gamma))
    print("Epsilon rate: " + str(epsilon))
    print("Product of gamma and epsilon rates (power consumption): " + str(gamma * epsilon))


if __name__ == "__main__":
    main()
