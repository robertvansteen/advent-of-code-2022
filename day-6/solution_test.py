import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def testPartOne(self):
        input = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
        self.assertEqual(solution(input, 4), 5)
        input = 'nppdvjthqldpwncqszvftbrmjlhg'
        self.assertEqual(solution(input, 4), 6)
        input = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
        self.assertEqual(solution(input, 4), 10)
        input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
        self.assertEqual(solution(input, 4), 11)

    def testPartTwo(self):
        input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
        self.assertEqual(solution(input, 14), 19)
        input = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
        self.assertEqual(solution(input, 14), 23)
        input = 'nppdvjthqldpwncqszvftbrmjlhg'
        self.assertEqual(solution(input, 14), 23)
        input = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
        self.assertEqual(solution(input, 14), 29)
        input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
        self.assertEqual(solution(input, 14), 26)
    
if __name__ == '__main__':
    unittest.main()
