def print_formatted(number):
    # your code goes here
    w = len(bin(n)[2:])
    for x in range(1, number+1):
        print(repr(x).rjust(w),
              (oct(x)).lstrip('0o').rjust(w),
              hex(x).lstrip('0x').upper().rjust(w),
              bin(x).lstrip('0b').rjust(w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
