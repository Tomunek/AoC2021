# --- Day 4: Giant Squid ---

def main():
    # this number is bigger then the first sum
    prev = 100000000
    larger_sums = 0
    measurements = []
    with open("input.txt") as f:
        measurements = f.readlines()
    for i in range(0, len(measurements) - 2):
        sum3 = int(measurements[i]) + int(measurements[i + 1]) + int(measurements[i + 2])
        if sum3 > prev:
            larger_sums += 1
        prev = sum3
    print("Number of sums larger than the previous sum: " + str(larger_sums))


if __name__ == "__main__":
    main()
