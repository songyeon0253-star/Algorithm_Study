import heapq

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 지도의 크기

    graph = [list(map(int, input())) for _ in range(N)]

    # 다익스트라
    distance = [[float('inf')] * N for _ in range(N)]

    def dijkstra():
        h = []
        heapq.heappush(h, (0, 0, 0)) # (0,0)에서 출발
        distance[0][0] = 0

        while h:
            dist, y, x = heapq.heappop(h)

            # 이미 방문한 경우 제외
            if distance[y][x] < dist: continue
            
            for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
                yy = y + dy
                xx = x + dx
                if yy<0 or xx<0 or yy>=N or xx>=N: continue # 범위 벗어나는 경우 제외

                cost = dist + graph[yy][xx]
                if cost < distance[yy][xx]:
                    heapq.heappush(h, (cost, yy, xx))
                    distance[yy][xx] = cost

        return distance[N-1][N-1]
    
    print(f'#{tc} {dijkstra()}')