# --- Day 8: Seven Segment Search ---

# def code_to_digit(code: str) -> int:
# code_map = {
#     "abcefg": 0,
#     "cf": 1,
#     "acdeg": 2,
#     "acdfg": 3,
#     "bcdf": 4,
#     "abdfg": 5,
#     "abdefg": 6,
#     "acf": 7,
#     "abcdefg": 8,
#     "abcdfg": 9
# }
# patterns:
# 1 - 2 characters (c,f)
# 2 - 5 characters + 3 and 5 found
# 3 - 5 characters + all characters from 1
# 4 - 4 characters (b,c,d,f)
# 5 - 5 characters - 9 without one of the characters from 1
# 6 - 6 characters - NOT 7
# 7 - 3 characters (a,c,f)
# 8 - 7 characters (all)
# 9 - 6 characters + all characters from 4
# 0 - 6 characters - NOT 6 and NOT 9
# sorted_code = ''.join(sorted(code, key=str.lower))
# return code_map[sorted_code]


class Note:

    def __init__(self):
        self.line_sample = []
        self.line_output = []
        self.digit_map = ["" for i in range(10)]
        pass

    def fill(self, line: [str]):
        self.line_sample = line[0].split(" ")
        self.line_output = line[1].split(" ")
        for i in range(len(self.line_sample)):
            self.line_sample[i] = ''.join(sorted(self.line_sample[i], key=str.lower))
        for i in range(len(self.line_output)):
            self.line_output[i] = ''.join(sorted(self.line_output[i], key=str.lower))

    def is_fully_mapped(self) -> bool:
        for i in self.digit_map:
            if i == "":
                return False
        return True

    def is_output_readable(self) -> bool:
        output = self.get_output()
        for c in output:
            if c == -1:
                return False
        return True

    def is_digit_found(self, digit: int) -> bool:
        if self.digit_map[digit] == "":
            return False
        return True

    def signal_to_digit(self, signal) -> int:
        for i in range(len(self.digit_map)):
            if self.digit_map[i] == signal:
                return i
        return -1

    def remove_from_samples(self, signal):
        for i in range(len(self.line_sample)):
            if self.line_sample[i] == signal:
                self.line_sample[i] = str(self.signal_to_digit(signal))

    def process(self):
        while not self.is_output_readable():
            for i in range(len(self.line_sample)):
                # already "consumed" signal
                if len(self.line_sample[i]) == 1:
                    continue

                # 0:
                if len(self.line_sample[i]) == 6 and self.is_digit_found(6) and self.is_digit_found(9):
                    self.digit_map[0] = self.line_sample[i]
                    self.remove_from_samples(self.line_sample[i])
                    continue

                # 1:
                if len(self.line_sample[i]) == 2:
                    self.digit_map[1] = self.line_sample[i]
                    self.remove_from_samples(self.line_sample[i])
                    continue

                # 2:
                if len(self.line_sample[i]) == 5 and self.is_digit_found(3) and self.is_digit_found(5):
                    self.digit_map[2] = self.line_sample[i]
                    self.remove_from_samples(self.line_sample[i])
                    continue

                # 3:
                if len(self.line_sample[i]) == 5 and self.is_digit_found(1):
                    contains = True
                    for char in self.digit_map[1]:
                        if char in self.line_sample[i]:
                            continue
                        else:
                            contains = False
                    if contains:
                        self.digit_map[3] = self.line_sample[i]
                        self.remove_from_samples(self.line_sample[i])
                        continue

                # 4:
                if len(self.line_sample[i]) == 4:
                    self.digit_map[4] = self.line_sample[i]
                    self.remove_from_samples(self.line_sample[i])
                    continue

                # 5:
                if len(self.line_sample[i]) == 5 and self.is_digit_found(9) and self.is_digit_found(1):
                    test1 = self.line_sample[i] == self.digit_map[9].replace(self.digit_map[1][0], '')
                    test2 = self.line_sample[i] == self.digit_map[9].replace(self.digit_map[1][1], '')
                    if test1 or test2:
                        self.digit_map[5] = self.line_sample[i]
                        self.remove_from_samples(self.line_sample[i])
                        continue

                # 6:
                if len(self.line_sample[i]) == 6 and self.is_digit_found(7):
                    cnt = 0
                    for char in self.digit_map[7]:
                        if char in self.line_sample[i]:
                            cnt += 1

                    if cnt == 2:
                        self.digit_map[6] = self.line_sample[i]
                        self.remove_from_samples(self.line_sample[i])
                        continue

                # 7:
                if len(self.line_sample[i]) == 3:
                    self.digit_map[7] = self.line_sample[i]
                    self.remove_from_samples(self.line_sample[i])
                    continue

                # 8:
                if len(self.line_sample[i]) == 7:
                    self.digit_map[8] = self.line_sample[i]
                    self.remove_from_samples(self.line_sample[i])
                    continue

                # 9:
                if len(self.line_sample[i]) == 6 and self.is_digit_found(4):
                    contains = True
                    for char in self.digit_map[4]:
                        if char in self.line_sample[i]:
                            continue
                        else:
                            contains = False
                    if contains:
                        self.digit_map[9] = self.line_sample[i]
                        self.remove_from_samples(self.line_sample[i])
                        continue

    def get_output(self) -> [int]:
        output = []
        for signal in self.line_output:
            output.append(self.signal_to_digit(signal))
        return output

    def to_string(self) -> str:
        out_str = ""
        for i in self.line_sample:
            out_str += i + " "
        out_str += "| "
        for i in self.line_output:
            out_str += i + " "
        return out_str


def main():
    signals = []

    with open("input.txt") as f:
        lines = f.readlines()
        signals = [Note() for i in range(len(lines))]
        for i in range(len(lines)):
            signals[i].fill(lines[i].split('\n')[0].split(" | "))

    outputs_sum = 0
    for row in signals:
        row.process()
        outputs = row.get_output()
        print(outputs)
        number = ""
        for char in outputs:
            number += str(char)
        outputs_sum += int(number)

    print(f"The sum of all the outputs is {outputs_sum}")


if __name__ == "__main__":
    main()
