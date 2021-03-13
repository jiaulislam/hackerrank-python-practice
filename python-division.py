if __name__ == '__main__':
    a = int(input())
    b = int(input())
    ans = [a//b, a/b]
    print("\n".join(list(map(str, ans))))
