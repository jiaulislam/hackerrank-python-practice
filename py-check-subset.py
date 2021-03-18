def solver_function(n: int):
    for _ in range(n):
        input()
        set_A = set(map(int, input().split()))
        input()
        set_B = set(map(int, input().split()))
        if set_A.intersection(set_B) == set_A or set_A.union(set_B) == set_B:
            print(True)
        else:
            print(False)
if __name__=="__main__":
    n = int(input())
    solver_function(n)