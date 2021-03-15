from collections import Counter

input()
shoe_sizes = Counter(list(map(int, input().strip().split())))

sum = 0
zz = int(input())
for _ in range(zz):
    key, value = map(int, input().split())
    isAvailable = shoe_sizes.get(key, 0)
    if isAvailable != 0:
        shoe_sizes[key] -= 1
        sum+=value
        # print(shoe_sizes.get(key))
print(sum)