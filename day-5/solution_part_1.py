import os 

def solution(input):
    stacks, instructions = input.split('\n\n')
    stacks = stacks.splitlines()[:-1][::-1]
    stacks = [''.join(j).rstrip() for i, j in enumerate(zip(*stacks)) if i % 4 == 1]

    for instruction in instructions.splitlines():
        count, src, dest = [int(x) for x in instruction.split() if x.isnumeric()] 
        src = src - 1
        dest = dest - 1
        stacks[dest] += stacks[src][-count:][::-1]
        stacks[src] = stacks[src][:-count]
    
    return ''.join([x[-1:] for x in stacks])

if __name__ == '__main__':
    input = open(os.path.dirname(__file__)+'/input', 'r').read()
    print(solution(input))