def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-1):
        subset = string[i:len(sub_string)+i]
        # print(repr(subset), repr(sub_string))
        if subset == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
