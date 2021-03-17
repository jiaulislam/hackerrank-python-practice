from itertools import groupby

if __name__ == "__main__":
    string = input()

    iterator = groupby(string)
    groups = []
    for key, group in iterator:
        groups.append((len(list(group)),int(key)))
    
    print(" ".join(str(x) for x in groups))
        
