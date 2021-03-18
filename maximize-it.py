from itertools import product


def square(x):
    return x**2


def solver(n, k):
    data = []
    smax = []

    for _ in range(n):
        nums = list(map(int, input().split()))[1:]
        data.append(nums)
    
    for numList in product(*data):
        powers=[]
        print(numList)
        for num in numList:
            powers.append(square(num))
        maxx = sum(powers)%k
        smax.append(maxx)
    print(max(smax))


if __name__ == "__main__":
    n, k = map(int, input().split())
    solver(n, k)
