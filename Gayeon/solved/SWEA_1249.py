import heapq

# delta
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dijkstra(start):
    a = len(arr)
    # 2차원 inf배열 -> 최소 누적 시간 갱신 예정
    result = [[float('inf')] * a for _ in range(a)]
    result[0][0] = 0
    pq = [(0, start)]

    while pq:
        cost, now = heapq.heappop(pq)
        y, x = now
        # 전략 1. result값보다 cost가 더 크면 continue
        if result[y][x] < cost: continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
            next_cost = arr[ny][nx]
            cost_sum = cost + next_cost

            # 전략 2. 누적값이 result보다 작으면 갱신
            if cost_sum < result[ny][nx]:
                result[ny][nx] = cost_sum
                # 다음 갈 곳 예약
                heapq.heappush(pq, (cost_sum, (ny, nx)))
    return result[n-1][n-1]


# main
T = int(input())
for tc in range(1, T+1):
    n = int(input()) # 지도 크기
    arr = [list(map(int, input())) for _ in range(n)]
    start = (0, 0)

    answer = dijkstra(start)
    print(f'#{tc} {answer}')