"""
11729번 : 하노이 탑 이동순서
재귀, python

n-1번째 탑을 1에서 2로 이동시킨 후
1에서 3으로 n번째 요소를 이동
n-1을 2에서 3으로 이동
"""

n = int(input())
order = list()

def hanoi(num, a, b, c):
    global order
    if num == 1:
        order.append(' '.join(map(str, [a, c])))
    else:
        hanoi(num-1, a, c, b)
        order.append(' '.join(map(str, [a, c])))
        hanoi(num-1, b, a, c)


hanoi(n, 1, 2, 3)

print(len(order))
for line in order:
    print(line)