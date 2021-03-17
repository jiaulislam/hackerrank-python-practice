from collections import OrderedDict, Counter

od = OrderedDict()

for i in range(int(input())):
    od[i] = input()
    
ctr = Counter(c for a, c in od.items())
print(len(ctr))
print(*ctr.values())