M = int(input())
m_set = set(map(int, input().strip().split()))
N = int(input())
n_set = set(map(int, input().strip().split()))

diff = [x for x in m_set.difference(n_set)]+[y for y in n_set.difference(m_set)]
print("\n".join(str(x) for x in sorted(diff)))
