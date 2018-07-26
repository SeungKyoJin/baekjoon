# 1011
'''
https://www.acmicpc.net/problem/1011
I solved this problem through addition before this version. 
However, if the limit of input value is much larger than usual, multipication is needed
to reduce the time complexity.
'''

import sys
import math

num = int(sys.stdin.readline())

max_ = 0
for i in range(num):
    cnt = 0
    lst = list(map(int, sys.stdin.readline().split()))

    distance = lst[1]-lst[0]

    temp = int(math.sqrt(distance))

    if pow(temp, 2) == distance:
        print(temp*2-1)
    elif pow(temp, 2) < distance and pow(temp, 2) + temp < distance:
        print(temp*2+1)
    elif pow(temp, 2) < distance and pow(temp, 2) + temp >= distance:
        print(temp*2)

