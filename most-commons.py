from collections import Counter 

def solver(n):
    c = Counter(sorted(n))
    for k , v in c.most_common(3):
        print(k, v)

if __name__ == "__main__":
    # n = int(input())
    string = input()
    solver(string)