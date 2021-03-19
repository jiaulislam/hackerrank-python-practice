cube = lambda x:  x**3

def fibonacci(n):
    sequence = []
    for i in range(n):
        if i < 2:
            sequence.append(i)
        elif i >= 2:
            fib = sequence[i-1] + sequence[i-2]
            sequence.append(fib)
    return sequence



if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
