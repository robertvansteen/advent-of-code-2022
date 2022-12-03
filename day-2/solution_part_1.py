import os 

def solution(input):
    return sum(iterate(input))

def iterate(input: str):
    for oponnent, player in map(str.split, input.splitlines()):
        oponnent = ord(oponnent) - ord('A')
        player = ord(player) - ord('X')
        yield (1 + player) + (oponnent - (player + 1)) % 3 * 3

if __name__ == '__main__':
    input = open(os.path.dirname(__file__)+'/input', 'r').read()
    print(solution(input))