from itertools import combinations

def solver(n):
    chars = list(input().split())
    K = int(input())
    comb = list(combinations(chars, K))
    a = [x for x in comb if 'a' in x]
    print(f'{round((len(a)/len(comb)),3)}')

if __name__ == "__main__":
    n = int(input())
    solver(n)
