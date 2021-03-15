from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# for i in product(A,B):
#     print(i, end=' ')

print(" ".join(str(x) for x in product(A,B)))