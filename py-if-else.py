def print_weird():
    print("Weird")


def print_not_weird():
    print("Not Weird")


if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print_weird()
    elif n % 2 == 0 and (n >= 2 and n <= 5):
        print_not_weird()
    elif n % 2 == 0 and (n >= 6 and n <= 20):
        print_weird()
    else:
        print_not_weird()
