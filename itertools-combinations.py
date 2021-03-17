from itertools import combinations

string , k = input().split()

for i in range(1,int(k)+1):
    for j in combinations(sorted(string), i):
        print("".join(j))