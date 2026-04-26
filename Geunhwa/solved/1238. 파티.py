import heapq

N, M, X = map(int, input().split()) # 마을 수, 도로 수, 목적지 마을

graph = [[] for _ in range(M+1)]

for _ in range(M):
    start, end, T = map(int, input().split()) # 시작점, 끝점, 소요시간
    graph[start].append((end, T))

# 다익스트라
def dijkstra(start, end):
    distance = [float('inf')] * (N+1)

    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0

    while h:
        dist, now = heapq.heappop(h)
        
        # 이미 처리된 노드일 경우 제외
        if distance[now] < dist: continue

        for a, b in graph[now]:
            cost = dist + b

            # 새로운 거리가 더 가까울 경우 추가해줌
            if cost < distance[a]:
                heapq.heappush(h, (cost, a))
                distance[a] = cost

    return distance[end]

ans = 0
# 모든 학생들 중 오고 가는데 가장 오래 걸리는 소요시간 구하기
for i in range(1, 1 + N):
    d1 = dijkstra(i, X) # X 마을로 가는 시간
    d2 = dijkstra(X, i) # 다시 돌아오는 시간

    ans = max(ans, d1+d2)

print(ans)

