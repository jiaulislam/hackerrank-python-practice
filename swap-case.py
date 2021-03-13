if __name__ == "__main__":
    string = input()
    
    print("".join(x.upper() if x.islower() else x.lower() for x in string))
