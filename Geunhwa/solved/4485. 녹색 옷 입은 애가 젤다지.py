import heapq

T = 1
while True:
    N = int(input()) # 동굴의 크기
    if N == 0: break # N = 0일 경우, 전체 입력 종료

    graph = [list(map(int, input().split())) for _ in range(N)]

    # 다익스트라
    distance = [[float('inf')] * N for _ in range(N)] 

    def dijkstra():
        h = []
        heapq.heappush(h, (graph[0][0], 0, 0)) # 0,0 에서 시작
        distance[0][0] = graph[0][0]

        while h:
            dist, y, x = heapq.heappop(h)

            # 이미 방문한 경우 제외
            if dist > distance[y][x]: continue

            for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
                yy = y + dy
                xx = x + dx
                if yy<0 or xx<0 or xx>=N or yy>=N: continue

                cost = dist + graph[yy][xx]

                if cost < distance[yy][xx]:
                    heapq.heappush(h, (cost, yy, xx))
                    distance[yy][xx] = cost
    dijkstra()

    print(f'Problem {T}: {distance[N-1][N-1]}')
    T += 1


