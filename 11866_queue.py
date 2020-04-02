"""
11866 요세푸스 문제0
queue
"""

n1, n2 = map(int, input().split())

q = [i for i in range(1, n1+1)]
res = list()

while len(q) != 0:
    for i in range(n2):
        if i == n2-1:
            res.append(q.pop(0))
        else:
            q.append(q.pop(0))

res = str(res)
res = res.replace('[', '<')
res = res.replace(']', '>')

print(res)