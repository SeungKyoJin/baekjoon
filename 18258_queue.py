"""
18258, 큐 2
다수의 입력을 받는 경우 표준입출력 사용
큐를 삽입할때 한칸씩 밀려야하니까 O(n)의 비용이 들어감
이걸 O(1)로 하지 못하면 시간초과
"""
import sys
from collections import deque

num = int(sys.stdin.readline())
q = deque()

def front(q):
    return q[0] if len(q) != 0 else -1

def back(q):
    return q[-1] if len(q) != 0 else -1

def size(q):
    return len(q)

def empty(q):
    return 1 if len(q) == 0 else 0

def pop(q):
    return q.popleft() if len(q) != 0 else -1

queue = {
    "front": front,
    "back": back,
    "size": size,
    "empty": empty,
    "pop": pop
}

for i in range(num):
    line = sys.stdin.readline().strip()
    if "u" in line:
        q.append(line.split()[1])
    else:
        print(queue[line](q))

