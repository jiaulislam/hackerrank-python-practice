def merge_the_tools(string, k):
    sub_list = [string[i:i+k] for i in range(0, len(string), k)]    
    for x in sub_list:
        get_set = set(x)
        print("".join(str(x) for x in get_set))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)