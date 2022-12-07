import os 
from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)

def solution(input: str):
    path = []
    dirs = {}

    for line in input.splitlines():
        match line.split():
            case "$", "cd", "/":
                path.append('/')
            case "$", "cd", "..":
                path.pop()
            case "$", "cd", dir:
                path.append(dir + '/')
            case "$" | "dir", *x:
                continue;
            case size, *x:
                for index, x in enumerate(path):
                    x = ''.join(path[:index + 1])
                    if not x in dirs: dirs.update({ x: 0 })
                    dirs[x] += int(size) 

    return sum(size for size in dirs.values() if size <= 100000)

if __name__ == '__main__':
    input = open(os.path.dirname(__file__)+'/input', 'r').read()
    print(solution(input))