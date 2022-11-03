# --- Day 1: Sonar Sweep ---

def main():
    # this number is bigger then the first measurement
    prev = 100000000
    larger_measurements = 0
    with open("input.txt") as f:
        for line in f.readlines():
            if int(line) > prev:
                larger_measurements += 1
            prev = int(line)
    print("Number of measurements larger than the previous measurement: " + str(larger_measurements))


if __name__ == "__main__":
    main()
