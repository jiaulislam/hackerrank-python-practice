if __name__ == "__main__":
    input()
    A = set(map(int, input().strip().split()))
    N = int(input())
    for i in range(N):
        operation = input().strip().split()
        if operation[0] == 'intersection_update':
            A.intersection_update(set(map(int,input().strip().split())))
        elif operation[0] == 'update':
            A.update(set(map(int, input().strip().split())))
        elif operation[0] == 'symmetric_difference_update':
            A.symmetric_difference_update(set(map(int, input().split())))
        elif operation[0] == 'difference_update':
            A.difference_update(set(map(int, input().strip().split())))

    print(sum(A))
