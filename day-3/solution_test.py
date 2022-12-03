import unittest
from solution_part_1 import solution as solutionOne
from solution_part_2 import solution as solutionTwo

class TestSolution(unittest.TestCase):
    def testPartOne(self):
        input = 'vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw'
        self.assertEqual(solutionOne(input), 157)
    
    def testPartTwo(self):
        input = 'vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw'
        self.assertEqual(solutionTwo(input), 70)

if __name__ == '__main__':
    unittest.main()
