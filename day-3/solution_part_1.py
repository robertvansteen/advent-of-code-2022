import os 

mod = ord('a') - ord('A') + 26

def solution(input):
    return sum(iterate(input))

def iterate(input: str):
    for line in input.splitlines():
        common = set(line[:len(line)//2]) & set(line[len(line)//2:])
        yield sum([(ord(letter) - ord('a')) % mod + 1 for letter in common])

if __name__ == '__main__':
    input = open(os.path.dirname(__file__)+'/input', 'r').read()
    print(solution(input))