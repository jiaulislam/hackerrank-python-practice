if __name__=="__main__":
    N = int(input())
    list = []
    for _ in range(N):
        action, *value = input().strip().split()
        if action == 'append' and len(value) == 1:
            list.append(int(value[0]))
        elif action == 'insert':
            list.insert(int(value[0]), int(value[1]))
        elif action == 'remove':
            list.remove(int(value[0]))
        elif action == 'sort':
            list.sort()
        elif action == 'pop':
            list.pop()
        elif action == 'reverse':
            list.reverse()
        elif action == 'print':
            print(list)
