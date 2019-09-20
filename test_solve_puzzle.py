from unittest import TestCase, main
from solve_puzzle import solve_puzzle


class TestSolvePuzzle(TestCase):

    def test_solve_puzzle(self):

        # [B, D, C, A]
        # [1, 3, 2, 0]
        solved = solve_puzzle('Please solve this puzzle:\n ABCD\nA=-->\nB--<-\nC--=<\nD-->-\n')
        self.assertEqual(solved, ' ABCD\nA=>>>\nB<=<<\nC<>=<\nD<>>=')

        # [C, D, B, A]
        # [2, 3, 1, 0]
        solved = solve_puzzle('Please solve this puzzle:\n ABCD\nA->--\nB-=->\nC--=<\nD-<--\n')
        self.assertEqual(solved, ' ABCD\nA=>>>\nB<=>>\nC<<=<\nD<<>=')


if __name__ == "__main__":
    main()
