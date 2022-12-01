import os

def main():
    list = sumList()
    print("Part one: "+ str(list[0]))
    print("Part two: "+ str(sum(list[:3])))

def sumList():
    input = open(os.path.dirname(__file__)+'/input', 'r').read()
    return sorted(iterate(input), reverse=True)

def iterate(input: str):
    for group in input.split('\n\n'):
        yield sum(int(line) for line in group.split('\n'))

main()