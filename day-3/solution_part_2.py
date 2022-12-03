import os 

mod = ord('a') - ord('A') + 26

def solution(input):
    return sum(iterate(input))

def iterate(input: str):
    for a, b, c in zip(*[iter(input.splitlines())] * 3):
        common = set(a) & set(b) & set(c)
        yield sum([(ord(letter) - ord('a')) % mod + 1 for letter in common])

if __name__ == '__main__':
    input = open(os.path.dirname(__file__)+'/input', 'r').read()
    print(solution(input))