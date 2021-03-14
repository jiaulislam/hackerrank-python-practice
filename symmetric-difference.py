M = int(input())
m_set = set(map(int, input().strip().split()))
N = int(input())
n_set = set(map(int, input().strip().split()))

diff = []
diff.append(x for x in list(map(int, m_set.difference(n_set))))
diff.append(x for x in list(map(int, n_set.difference(m_set))))

print(diff)
