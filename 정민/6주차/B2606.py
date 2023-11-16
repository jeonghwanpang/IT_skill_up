# 백준 2606번 바이러스 (실버3)

count = 0
def dfs(graph, v, visited):
    global count
    visited[v] = True
    count += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n = int(input())
m = int(input())

graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
  a, b = map(int, input().split())

  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (len(graph) + 1)
dfs(graph, 1, visited)
print(count - 1)