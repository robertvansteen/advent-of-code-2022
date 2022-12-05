import unittest
from solution_part_1 import solution as solutionOne
from solution_part_2 import solution as solutionTwo

class TestSolution(unittest.TestCase):
    def testPartOne(self):
        input = '    [D]    \n[N] [C]    \n[Z] [M] [P]\n1   2   3\n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2'
        self.assertEqual(solutionOne(input), 'CMZ')
    
    def testPartTwo(self):
        input = '    [D]    \n[N] [C]    \n[Z] [M] [P]\n1   2   3\n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2'
        self.assertEqual(solutionTwo(input), 'MCD')

if __name__ == '__main__':
    unittest.main()
