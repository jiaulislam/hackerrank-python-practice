from itertools import combinations_with_replacement

def print_comb(string, k):
    combinations = combinations_with_replacement(sorted(string), int(k))

    for comb in combinations:
        print("".join(str(x) for x in comb))

if __name__=="__main__":
    string, k = input().split()

    print_comb(string, k)