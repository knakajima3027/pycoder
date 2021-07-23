from main_A import solve
import unittest


class solveTest(unittest.TestCase):

    def test_sample(self):
        test_cases = [[5, 3, 20, 15, 90], [10, 10, 100, 1, 1000]]
        for test_case in test_cases:
            res = solve(test_case[0], test_case[1], test_case[2], test_case[3])
            self.assertEqual(res, test_case[4])

if __name__ == "__main__":
    unittest.main()
