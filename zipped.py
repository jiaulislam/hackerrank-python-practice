def solver(students, subjects):
    lst = []
    for _ in range(subjects):
        lst.append(map(float, [x for x in input().split()]))

    for marks in zip(*lst):
        print((sum(marks)/subjects))

if __name__ == "__main__":
    N, X = map(int, input().split())
    solver(N,X)
