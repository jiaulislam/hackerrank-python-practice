from datetime import datetime


if __name__=="__main__":
    n = int(input())

    # according to the problem should be this parser
    parser = "%a %d %b %Y %H:%M:%S %z"

    for _ in range(n):
        d1 = datetime.strptime(input(), parser)
        d2 = datetime.strptime(input(), parser)
        print(int(abs(d1-d2).total_seconds()))