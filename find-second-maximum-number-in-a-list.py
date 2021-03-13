from collections import Counter

if __name__ == '__main__':
    n = int(input())
    arr = sorted(Counter(map(int, input().split())))
    print(arr[-2])
