import unittest
from solution_part_1 import solution as solutionOne
from solution_part_2 import solution as solutionTwo

class TestSolution(unittest.TestCase):
    def testPartOne(self):
        input = '2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8'
        self.assertEqual(solutionOne(input), 2)
    
    def testPartTwo(self):
        input = '2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8'
        self.assertEqual(solutionTwo(input), 4)

if __name__ == '__main__':
    unittest.main()
