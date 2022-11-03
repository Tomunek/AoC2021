# --- Day 2: Dive! ---

def main():
    hor_pos = 0
    depth = 0
    with open("input.txt") as f:
        for line in f.readlines():
            command = line.split(" ")[0]
            value = int(line.split(" ")[1])
            # print("Command: \"" + command + "\" Value: " + str(value))
            if command == "forward":
                hor_pos += value
            elif command == "down":
                depth += value
            elif command == "up":
                depth -= value

    print("Horizontal position: " + str(hor_pos))
    print("Vertical position: " + str(depth))
    print("Product of horizontal and vertical positions: " + str(hor_pos * depth))


if __name__ == "__main__":
    main()