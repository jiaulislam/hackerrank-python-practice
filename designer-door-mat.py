"""
 Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------


        Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

"""
import math
row, cols = map(int, input().split())
middle = row//2+1

for i in range(1, middle):
    center = (i*2-1)*".|."
    print(center.center(cols, "-"))
print("WELCOME".center(cols, "-"))
for i in reversed(range(1, middle)):
    center = (i*2-1)*".|."
    print(center.center(cols, "-"))