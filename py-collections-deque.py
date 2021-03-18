from collections import deque


def solver(n):
    que = deque()
    for _ in range(n):
        command, sep , value = input().partition(" ")
        if command == "append":
            que.append(int(value))
        elif command == "appendleft":
            que.appendleft(int(value))
        elif command == "pop":
            que.pop()
        elif command == "popleft":
            que.popleft()
    print(" ".join(str(x) for x in que))

if __name__ == "__main__":
    n = int(input())
    solver(n)
