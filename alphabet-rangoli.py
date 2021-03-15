from string import ascii_lowercase as chars

def print_rangoli(size):
    line = []
    width = 4 * size - 3
    for i in range(size):
        s = "-".join(chars[i:n])
        # s[::-1] is reverse of c-b-a and s[1:] is b-c
        line.append((s[::-1]+s[1:]).center(width,"-"))
        # print(line)

    # pick the list last item + 
    print("\n".join(line[:0:-1]+line))
    # print(line)
    # print(line[:0:-1])

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
