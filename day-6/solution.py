import os 

def solution(input: str, distinct: int):
    return next((x for x in range(len(input)) if len(set(input[x-distinct:x])) == distinct), None)

if __name__ == '__main__':
    input = open(os.path.dirname(__file__)+'/input', 'r').read()
    print(solution(input, 4))
    print(solution(input, 14))