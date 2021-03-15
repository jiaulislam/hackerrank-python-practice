from itertools import permutations


string, k = map(str, input().split())

permut = permutations(string, int(k))

for i in sorted(permut):
    print("".join(i))