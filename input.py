# only for python 2



if __name__ == "__main__":
    x, k = map(int, input().split())

    poly = input()
    print(True if eval(str(poly))==k else False)
