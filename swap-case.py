def swap_case(string):
    return("".join(x.upper() if x.islower() else x.lower() for x in string))


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
