from collections import deque

def solver(n):
    input()
    q = deque([int(x) for x in input().split()])
    print(q.index())
    while len(q):
        f, b = q.popleft(), q.pop()
        if f > b:
            pass

if __name__ == "__main__":
    n = int(input())
    solver(n)