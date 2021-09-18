

class Sudoku:

    def __init__(self, digits):
        self.nb_lines = 9
        self.nb_columns = 9
        self.zero_indexes = list()
        self.grid = self.create_grid(digits)
        self.all_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def create_grid(self, digits):
        sudoku = list()
        for line_index, i in enumerate(range(0, len(digits), self.nb_lines)):
            line = list()
            for column_index, digit in enumerate(digits[i:i + self.nb_lines]):
                digit = int(digit)
                line.append(digit)
                if digit == 0:
                    self.zero_indexes.append((line_index, column_index))
            sudoku.append(line)
        return sudoku

    def fill_digits_succeed(self, zero_index=0):
        try:
            line_index, column_index = self.zero_indexes[zero_index]
        except IndexError:
            return True
        digits_line = self.grid[line_index]
        digits_column = [line[column_index] for line in self.grid]
        digits_square = self.extract_square(line_index, column_index)
        digits = self.all_digits - set(digits_line) - set(digits_column) - set(digits_square)
        for digit in digits:
            digits_line[column_index] = digit
            if self.fill_digits_succeed(zero_index + 1):
                return True
        digits_line[column_index] = 0
        return False

    def extract_square(self, line_index, column_index):
        line_index = line_index + (line_index % 3) * -1
        column_index -= column_index % 3
        square = self.grid[line_index][column_index:column_index + 3]
        square += self.grid[line_index + 1][column_index:column_index + 3]
        square += self.grid[line_index + 2][column_index:column_index + 3]
        return square

    def grid_to_sdm(self):
        sdm = ''
        for line in self.grid:
            sdm += ''.join([str(digit) for digit in line])
        return sdm


def sudoku_solve(digits):
    sudoku = Sudoku(digits)
    succeed = sudoku.fill_digits_succeed()
    if not succeed:
        return 'Unsolvable'
    else:
        return sudoku.grid_to_sdm()


