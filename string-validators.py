def print_output(ss: str):
    print(any([x.isalnum() for x in ss]))
    print(any([x.isalpha() for x in ss]))
    print(any([x.isdigit() for x in ss]))
    print(any([x.islower() for x in ss]))
    print(any([x.isupper() for x in ss]))

if __name__ == '__main__':
    s = input()
    # print(string.ascii_letters)
    print_output(s)
