

if __name__ == "__main__":
    arr_length, sets = map(int, input().split())
    array = list(map(int, input().strip().split()))
    happy_set = set(map(int, input().strip().split()))
    sad_set = set(map(int, input().strip().split()))
    hapiness = 0

    for x in array:
        if x in happy_set:
            hapiness+=1
        if x in sad_set:
            hapiness-=1

    print(hapiness)