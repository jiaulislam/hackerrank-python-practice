def solve(s:str):
    ss = s.strip().split(" ")
    return " ".join(x.capitalize() if x.isalpha() else x for x in ss)


if __name__ == '__main__':
    s = input()
    print(solve(s))