import unittest
from solution_part_1 import solution as solutionPartOne
from solution_part_2 import solution as solutionPartTwo

class TestSolution(unittest.TestCase):
    def testPartOne(self):
        input = '$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k'
        self.assertEqual(solutionPartOne(input), 95437)

    def testPartTwo(self):
        input = '$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k'
        self.assertEqual(solutionPartTwo(input), 24933642)

if __name__ == '__main__':
    unittest.main()
