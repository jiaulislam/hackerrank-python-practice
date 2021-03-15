def minion_game(string):
    vowels = "AEIOU"
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if string[i] not in vowels:
            stuart += len(string)-i
        else:
            kevin += len(string)-i

    if stuart > kevin:
        ans = print("Stuart", stuart)
    elif kevin > stuart:
        ans = print("Kevin", kevin)
    else:
        ans = print("Draw")
    return ans


if __name__ == '__main__':
    s = input()
    minion_game(s)
