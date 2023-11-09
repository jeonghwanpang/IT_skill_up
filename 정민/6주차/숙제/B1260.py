# 백준 1260번 DFS와 BFS (실버2)

from collections import deque

def bfs(graph, root):
   visited = [False] * (n + 1)
   queue = deque([root])

   # 현재 노드를 방문 처리
   visited[root] = True

   # 큐가 빌 때까지 반복
   while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')

    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in sorted(graph[v]):
      if not visited[i]:
        queue.append(i)
        visited[i] = True


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)


n, m, v = map(int, input().split())

graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
  a, b = map(int, input().split())

  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
bfs(graph, v)