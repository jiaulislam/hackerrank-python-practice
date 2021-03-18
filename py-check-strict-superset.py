def solver():
    set_a = set(map(int, input().split()))
    n = int(input())
    strictSuperSet = True
    for _ in range(n):
        other_sets = set(map(int, input().split()))
        for n in other_sets:
            if n not in set_a:
                strictSuperSet = False
                break
    print(strictSuperSet)

if __name__== "__main__":
    solver()