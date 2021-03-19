def solver(n):
    a = list(map(int, input().split()))
    if all(x > 0 for x in a) and any(str(x) == str(x)[::-1] for x in a):
        print('True')
    else:
        print('False')


if __name__ == "__main__":
    n = int(input())
    solver(n)
