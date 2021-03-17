

if __name__ == "__main__":
    input()
    s = set(x for x in list(map(int, input().split())))
    num_of_operation = int(input())

    for _ in range(num_of_operation):
        operation, sep, val = input().partition(" ")

        if operation == 'pop':
            s.pop()
        elif operation == 'remove':
            try:
                s.remove(int(val.strip()))
            except KeyError:
                pass
        elif operation == 'discard':
            s.discard(int(val.strip()))

    print(sum(s))
    
