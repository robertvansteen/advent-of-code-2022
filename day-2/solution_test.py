import unittest
from solution_part_1 import solution as solutionPartOne
from solution_part_2 import solution as solutionPartTwo

class TestSolution(unittest.TestCase):
    def testPartOne(self):
        self.assertEqual(solutionPartOne('A Y\nB X\nC Z'), 15)

    def testPartTwo(self):
        self.assertEqual(solutionPartTwo('A Y\nB X\nC Z'), 12)

if __name__ == '__main__':
    unittest.main()
