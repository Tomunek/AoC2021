# --- Day 4: Giant Squid ---
class BingoField:
    value = -1
    chosen = False

    def __init__(self, new_value: int):
        self.value = new_value

    def set_value(self, new_value: int):
        self.value = int(new_value)

    def get_value(self) -> int:
        return self.value

    def choose(self):
        self.chosen = True

    def unchoose(self):
        self.chosen = False

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
            if int(field.get_value()) == number:
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
    return False


def get_partial_score(board: [[BingoField]]) -> int:
    unmarked_sum = 0
    for row in board:
        for field in row:
            if not field.is_chosen():
                unmarked_sum += int(field.get_value())
    return unmarked_sum


def print_board(board: [[BingoField]]):
    s_board = "["
    for row in board:
        s_board += "["
        for field in row:
            if bool(field.is_chosen()):
                s_board += "*" + str(field.get_value()) + ","
            else:
                s_board += str(field.get_value()) + ","
        s_board += "]\n"
    s_board += "]"
    return s_board


def destroy_board(board: [[BingoField]]):
    for row in board:
        for field in row:
            field.set_value(-1)
            field.unchoose()


def main():
    chosen_values = []
    boards = []
    boards_count = 0

    with open("input.txt") as f:
        chosen_numbers = f.readline()
        chosen_values_str = chosen_numbers.split(",")
        for val in chosen_values_str:
            chosen_values.append(int(val))
        boards_read = f.readlines()
        boards_count = int(len(boards_read) / 6)

    for i in range(boards_count):
        board = []
        for j in range(1, 6):
            board.append(add_row(boards_read[i * 6 + j].strip("\n").split(" ")))
        boards.append(board)

    print("Chosen numbers: ", chosen_values)
    print("Number of boards: " + str(boards_count))
    for board in boards:
        print(print_board(board))

    current_number = -1
    last_winning_board = 0
    last_winning_score = 0
    while current_number < len(chosen_values) - 1:
        current_number += 1
        for board in boards:
            choose_number(board, chosen_values[current_number])
        for board in boards:
            if is_won(board):
                last_winning_board = board
                last_winning_score = get_partial_score(board) * chosen_values[current_number]
                boards.pop(boards.index(board))

    print("Score of the last winning board: " + str(last_winning_score))


if __name__ == "__main__":
    main()
