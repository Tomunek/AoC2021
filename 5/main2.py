# --- Day 5: Hydrothermal Venture ---

def sign(i: int) -> int:
    if i < 0:
        return -1
    else:
        return 1


class Line:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def __init__(self, _x1: int, _y1: int, _x2: int, _y2: int):
        self.x1 = _x1
        self.y1 = _y1
        self.x2 = _x2
        self.y2 = _y2

    def to_str(self) -> str:
        line_string = f"{self.x1},{self.y1}->{self.x2},{self.y2}"
        return line_string

    def rotate(self):
        tmpx = self.x1
        tmpy = self.y1
        self.x1 = self.x2
        self.y1 = self.y2
        self.x2 = tmpx
        self.y2 = tmpx


class Board:
    board_size = 0
    vents = []

    def __init__(self, size: int):
        self.board_size = size
        assert (size > 1)
        self.vents = [[0 for y in range(self.board_size)] for x in range(self.board_size)]

    def add_vent_line(self, line: Line):
        print(line.to_str())

        # handle diagonal
        if line.x1 != line.x2 and line.y1 != line.y2:
            dx = line.x2 - line.x1
            dy = line.y2 - line.y1
            x = line.x1
            y = line.y1
            for i in range(abs(dx) + 1):
                print(f"Adding point: {x}:{y}")
                self.vents[x][y] += 1
                x += sign(dx)
                y += sign(dy)

            return

        # handle vertical / horizontal
        if line.x1 == line.x2:
            if line.y1 < line.y2:
                for y in range(line.y1, line.y2 + 1):
                    self.vents[line.x1][y] += 1
                    print(f"Adding point: {line.x1}:{y}")
            else:
                for y in range(line.y2, line.y1 + 1):
                    self.vents[line.x1][y] += 1
                    print(f"Adding point: {line.x1}:{y}")
        else:
            if line.x1 < line.x2:
                for x in range(line.x1, line.x2 + 1):
                    self.vents[x][line.y1] += 1
                    print(f"Adding point: {x}:{line.y1}")
            else:
                for x in range(line.x2, line.x1 + 1):
                    self.vents[x][line.y1] += 1
                    print(f"Adding point: {x}:{line.y1}")

    def to_str(self) -> str:
        board_string = ""
        for y in range(self.board_size):
            for x in range(self.board_size):
                board_string += str(self.vents[x][y])
            board_string += '\n'
        return board_string

    def count(self) -> [int]:
        counter = [0 for i in range(1000)]
        for row in self.vents:
            for fld in row:
                counter[fld] += 1
        return counter


def main():
    lines = []
    board = Board(1000)
    with open("input.txt") as f:
        for line in f.readlines():
            xy1, _, xy2 = line.split(' ')
            x1, y1 = xy1.split(',')
            x2, y2 = xy2.split(',')
            ln = Line(int(x1), int(y1), int(x2), int(y2))
            lines.append(ln)

    for line in lines:
        board.add_vent_line(line)

    # print(board.to_str())
    counter = board.count()

    how_many_ge_two = 0
    for i in range(len(counter)):
        if i >= 2:
            how_many_ge_two += counter[i]

    print(f"Number of points where two or more lines overlap: {how_many_ge_two}")


if __name__ == "__main__":
    main()
