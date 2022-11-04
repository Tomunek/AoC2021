# --- Day 4: Giant Squid ---
class BingoField:
    value = -1
    chosen = False

    def __init__(self):
        pass

    def __init__(self, new_value: int):
        self.value = new_value

    def set_value(self, new_value: int):
        self.value = new_value

    def get_value(self):
        return self.value

    def choose(self):
        self.chosen = True

    def is_chosen(self) -> bool:
        return self.chosen


def add_row(new_row: [str]) -> [BingoField]:
    row = []
    for field in new_row:
        if field != "":
            row.append(BingoField(field))
    return row


def choose_number(board: [[BingoField]], number: int):
    for row in board:
        for field in row:
            if field.get_value() == number:
                field.choose()


def is_won(board: [[BingoField]]) -> bool:
    for row in board:
        cnt = 0
        for field in row:
            if field.is_chosen():
                cnt += 1
        if cnt == 5:
            return True
    for i in range(5):
        cnt = 0
        for j in range(5):
            if board[j][i].is_chosen():
                cnt += 1
        if cnt == 5:
            return True
    for i in range(5):
        cnt = 0
        if board[i][i].is_chosen():
            cnt += 1
        if cnt == 5:
            return True
    for i in range(5):
        cnt = 0
        if board[i][4 - i].is_chosen():
            cnt += 1
        if cnt == 5:
            return True


def get_partial_score(board: [[BingoField]]) -> int:
    unmarked_sum = 0
    for row in board:
        for field in row:
            if not field.is_chosen:
                unmarked_sum += field.get_value()
    return unmarked_sum


def print_board(board: [[BingoField]]):
    s_board = "["
    for row in board:
        s_board += "["
        for field in row:
            if field.is_chosen():
                s_board += "*" + str(field.get_value()) + ","
            else:
                s_board += str(field.get_value()) + ","
        s_board += "]\n"
    s_board += "]"
    return s_board


def main():
    chosen_values = []
    boards = []
    boards_count = 0

    with open("example_input.txt") as f:
        chosen_numbers = f.readline()
        chosen_values_str = chosen_numbers.split(",")
        for val in chosen_values_str:
            chosen_values.append(int(val))
        boards_read = f.readlines()
        boards_count = int(len(boards_read) / 6)

    for i in range(boards_count):
        board = []
        for j in range(1, 6):
            print(i * 6 + j)
            board.append(add_row(boards_read[i * 6 + j].strip("\n").split(" ")))
        boards.append(board)

    print("Chosen numbers: ", chosen_values)
    print("Number of boards: " + str(boards_count))
    for board in boards:
        print(print_board(board))

    found_win = False
    current_number = -1
    score = 0
    while not found_win:
        current_number += 1
        for board in boards:
            choose_number(board, chosen_values[current_number])
        for board in boards:
            if is_won(board):
                found_win = True
                score = get_partial_score(board) * chosen_values[current_number]
    print("Score of the first winning board: " + score)


if __name__ == "__main__":
    main()