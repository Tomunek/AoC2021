# --- Day 9: Smoke Basin ---

def is_point_low(x: int, y: int, heightmap: [[int]], max_x: int, max_y: int) -> bool:
    is_low = True
    value = heightmap[x][y]
    if x - 1 >= 0:
        if heightmap[x - 1][y] <= value:
            is_low = False
    if y - 1 >= 0:
        if heightmap[x][y - 1] <= value:
            is_low = False
    if x + 1 < max_x:
        if heightmap[x + 1][y] <= value:
            is_low = False
    if y + 1 < max_y:
        if heightmap[x][y + 1] <= value:
            is_low = False
    return is_low


def main():
    heightmap = []
    max_x = 0
    max_y = 0

    with open("input.txt") as f:
        lines = f.readlines()

        for row in lines:
            heightmap_row = []
            for val in row:
                if val.isdigit():
                    heightmap_row.append(int(val))
            heightmap.append(heightmap_row)

    max_x = len(heightmap)
    max_y = len(heightmap[0])

    low_spots = []

    for x in range(max_x):
        for y in range(max_y):
            if is_point_low(x, y, heightmap, max_x, max_y):
                low_spots.append((x, y))

    print(f"Low spots: {low_spots}")

    risk_sum = 0
    for point in low_spots:
        risk_sum += heightmap[point[0]][point[1]] + 1

    print(f"Sum of all risk levels: {risk_sum}")


if __name__ == "__main__":
    main()
