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


def basin_neighbours(number: int, x: int, y: int, heightmap: [[int]], max_x: int, max_y: int, basin_map: [[int]]):
    if basin_map[x][y] == -1:
        basin_map[x][y] = number
        if x - 1 >= 0:
            if heightmap[x - 1][y] < 9:
                basin_neighbours(number, x - 1, y, heightmap, max_x, max_y, basin_map)
        if y - 1 >= 0:
            if heightmap[x][y - 1] < 9:
                basin_neighbours(number, x, y - 1, heightmap, max_x, max_y, basin_map)
        if x + 1 < max_x:
            if heightmap[x + 1][y] < 9:
                basin_neighbours(number, x + 1, y, heightmap, max_x, max_y, basin_map)
        if y + 1 < max_y:
            if heightmap[x][y + 1] < 9:
                basin_neighbours(number, x, y + 1, heightmap, max_x, max_y, basin_map)
        else:
            return


def find_basin(number: int, point: (int, int), heightmap: [[int]], max_x: int, max_y: int, basin_map: [[int]]):
    basin_neighbours(number, point[0], point[1], heightmap, max_x, max_y, basin_map)
    return


def get_basin_size(number: int, basin_map: [[int]]) -> int:
    basin_size = 0
    for row in basin_map:
        for val in row:
            if val == number:
                basin_size += 1
    return basin_size


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

    basin_map = []
    for x in range(max_x):
        basin_row = []
        for y in range(max_y):
            basin_row.append(-1)
        basin_map.append(basin_row)

    for number in range(len(low_spots)):
        find_basin(number, low_spots[number], heightmap, max_x, max_y, basin_map)

    largest_basins = [-1, -1, -1]
    basin_sizes = []

    for i in range(len(low_spots)):
        size = get_basin_size(i, basin_map)
        if size > largest_basins[2]:
            largest_basins[0] = largest_basins[1]
            largest_basins[1] = largest_basins[2]
            largest_basins[2] = size
            continue
        if size > largest_basins[1]:
            largest_basins[0] = largest_basins[1]
            largest_basins[1] = size
            continue
        if size > largest_basins[0]:
            largest_basins[0] = size
            continue

    largest_basins_product = largest_basins[0] * largest_basins[1] * largest_basins[2]

    print(f"Product of 3 largest basin sizes: {largest_basins_product}")


if __name__ == "__main__":
    main()
