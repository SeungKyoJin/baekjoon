"""
2606, 바이러스
스택을 구현할 수 있나?
dfs를 구현할 수 있나?
"""
num_node = int(input())
num_edge = int(input())

graph = dict()

def dfs(graph, p):
    visited = list()
    stack = list()

    stack.append(p)
    while len(stack) != 0:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited

for i in range(num_edge):
    k, v = map(int, input().split())
    if graph.get(k) == None:
        graph[k] = [v]
    else:
        graph[k].append(v)

    if graph.get(v) == None:
        graph[v] = [k]
    else:
        graph[v].append(k)

res = dfs(graph, 1)
res.remove(1)

print(len(res))