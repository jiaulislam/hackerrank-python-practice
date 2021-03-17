if __name__ == "__main__":
    input()
    A = set(map(int, input().strip().split()))
    input()
    B = set(map(int, input().strip().split()))

    print(len(A.difference(B)))
