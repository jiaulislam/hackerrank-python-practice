from collections import Counter


if __name__ == "__main__":
    k = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    
    for k, v in c.items():
        if v == 1:
            print(k)