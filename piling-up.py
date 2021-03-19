from collections import deque
import sys

def solver(n):
    for _ in range(n):
        max_size = int(input())
        que = deque([int(x) for x in input().split()],maxlen=max_size)
        first , last = que[0], que[-1]
        cube = -sys.maxsize
        for _ in range(max_size):
            if first >= last:
                if cube >= first:
                    cube = first
                    que.popleft()
            else:
                if cube >= last:
                    cube = last
                    que.pop()
            # print(que)
        print("Yes" if len(que) == 0 else "No")

if __name__ == "__main__":
    n = int(input())
    solver(n)
