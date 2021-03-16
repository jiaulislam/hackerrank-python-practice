import math

DEGREE = u"\N{DEGREE SIGN}"

def tanInverse(x, y):
    return round(math.degrees(math.atan(x/y)))

if __name__=="__main__":
    AB = int(input())
    BC = int(input())
    print(str(tanInverse(AB,BC))+DEGREE)
