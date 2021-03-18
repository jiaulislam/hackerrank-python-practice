def solver(n):
    for i in range(1,n+1):
        print(((10**i-1)//9)**2)

if __name__ == "__main__":
    n = int(input())
    solver(n)
