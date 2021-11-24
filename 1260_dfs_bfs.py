from collections import deque


def dfs(graph, begin, visited_list):
    b = begin - 1
    visited_list.append(b)
    print(begin, end=' ')

    for i, v in enumerate(graph[b]):
        if v == 1 and i not in visited_list:
            visited_list.append(i)
            dfs(graph, i + 1, visited_list)

    return 0

def bfs(graph, begin, visited_list):
    b = begin - 1
    q = deque()

    q.append(b)
    visited_list.append(b)
    print(begin, end=' ')

    while True:
        if len(q) == 0:
            break
        for i, v in enumerate(graph[q[0]]):
            if v == 1 and i not in visited_list:
                q.append(i)
                visited_list.append(i)
                print(i + 1, end=' ')
        q.popleft()

    return 0


int_v, int_e, begin = map(int, input().split())

graph = [[0] * int_v for i in range(int_v)]

for i in range(int_e):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
    graph[y - 1][x - 1] = 1

dfs(graph, begin, [])
print()
bfs(graph, begin, [])
