from main_B import solve
import unittest


class solveTest(unittest.TestCase):

    def test_sample(self):
        test_cases = [["00101", "Takahashi"], ["010", "Aoki"]]
        for test_case in test_cases:
            self.assertEquals(solve(test_case[0]), test_case[1])

if __name__ == "__main__":
    unittest.main()
