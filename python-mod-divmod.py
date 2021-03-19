def solver(n,k):
    print(n//k)
    print(n%k)
    print(divmod(n, k))

if __name__ == "__main__":
    n, k = map(int, input().strip().split(" "))
    solver(n,k)