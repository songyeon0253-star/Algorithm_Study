import heapq

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split()) # 마지막 연결지점 번호, 도로의 개수

    graph = [[] for _ in range(1001)]
    for _ in range(E):
        s, e, w = map(int, input().split())  # 구간 시작, 구간 끝, 구간 거리
        graph[s].append((e, w))

    # 다익스트라
    dist = [float('inf')] * 1001

    def dijkstra(start):
        h = []
        heapq.heappush(h, (0, start))
        dist[start] = 0

        while h:
            cost, now = heapq.heappop(h)

            if dist[now] < cost: continue

            for n, c in graph[now]:
                new_cost = cost + c

                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if dist[n] > new_cost:
                    dist[n] = new_cost
                    heapq.heappush(h, (new_cost, n))

    # 0번 지점부터 출발하는 최소 거리
    dijkstra(0)

    print(f'#{tc} {dist[N]}')






