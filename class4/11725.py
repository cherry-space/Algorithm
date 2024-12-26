from collections import deque

N = int(input())

graph = {i:[] for i in range(1, N+1)}
visited = [False]*(N+1)
answer = [0]*(N+1)   #답을 저장할 배열


for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
        
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                answer[i] = x
                visited[i] = True
                queue.append(i)


bfs(graph, 1, visited)
for i in range(2, N+1):
    print(answer[i])
    