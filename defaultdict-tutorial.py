from collections import defaultdict


if __name__=="__main__":
    a, b = map(int, input().strip().split())
    m = defaultdict(list)
    m_list = []
    n_list = []
    for i in range(a):
        m_list.append(input())
    for i in range(b):
        n_list.append(input())

    m[1] = m_list

    for n in n_list:
        if n in m.get(1):
            for i, value in enumerate(m.get(1)):
                if n == value:
                    print(f"{i+1}", end=' ')
        else:
            print("-1", end=" ")
        print()