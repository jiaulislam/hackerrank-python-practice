if __name__=="__main__":
    N = int(input())
    records = []
    scores = set()
    for _ in range(N):
        name = input().strip()
        grade = float(input())
        records.append([name,grade])
        scores.add(grade)
    second_lowest = sorted(scores)[1]
    second_lowest_names= []
    for name, score in records:
        if score == second_lowest:
            second_lowest_names.append(name)
    print("\n".join(map(str, second_lowest_names)))