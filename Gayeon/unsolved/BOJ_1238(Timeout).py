import heapq

def dijkstra(start, end):
    result = [float('inf')] * (N+1)
    result[0] = 0
    result[start] = 0

    pq = [(0, start)] # (비용, 현재 위치)
    while pq:
        cost, now = heapq.heappop(pq)
        if result[now] < cost: continue

        for i in range(1, N+1):
            if graph[now][i] == 0: continue
            cost_sum = graph[now][i] + cost

            if result[i] < cost_sum: continue
            result[i] = cost_sum
            heapq.heappush(pq, (cost_sum, i))
    return result[end]

# main
# 학생 수, 단방향 도로 수, 목적 마을
N, M, X = map(int, input().split())

graph = [[0]* (N+1) for _ in range(N+1)] # 비용 저장되는 배열
for _ in range(M):
    # 시작점, 끝점, 소요시간
    start, end, t = map(int, input().split())
    graph[start][end] = t


max_time = 0
for home in range(1, N+1):
    home_to_X = dijkstra(home, X) # 집 -> X 최단 시간
    X_to_home = dijkstra(X, home) # X -> 집 최단시간
    total = home_to_X + X_to_home
    if max_time < total:
        max_time = total
print(max_time)