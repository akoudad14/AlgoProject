import unittest

from sudokusolve import sudoku_solve


class SudokuSolveTestCase(unittest.TestCase):
    inputs = ["004006079000000602056092300078061030509000406020540890007410920105000000840600100",
              "010003000504600001037029060200060400040308010000000000000000000472000005005000236",
              "910000000520000300800020064003001000700058002000400800000000007400000005000070030",
              "000000207008000390001000000000028000000040003080007409250804000690100005007030000",
              "000039008000600200090006100000080053002000600730050000005200010004007000900310007",
              "000300708000209010017000000605037000000000000830500000000000490060708000090602300"]
    outputs = ["284136579913754682756892341478961235539287416621543897367415928195328764842679153",
               "916543728524687391837129564283761459749358612651492873368215947472936185195874236",
               "916543728524687391837129564283761459749358612651492873368215947472936185195874236",
               "935486217768251394421793568149328756572649183386517429253864971694172835817935642",
               "Unsolvable",
               "946315728358279614217486935625937841179824563834561279782153496463798152591642387"]

    def test_solver(self):
        for i, problem in enumerate(self.inputs):
            result = sudoku_solve(problem)
            self.assertEqual(result, self.outputs[i])


if __name__ == "__main__":
    unittest.main()