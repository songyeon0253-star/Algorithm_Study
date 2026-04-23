import heapq

def dijkstra(end_node):
    # inf 배열 생성 -> 최단 거리 갱신 예정
    A = end_node + 1
    result = [float('inf')] * A
    result[0] = 0

    q = [(0, 0)] # (현재 비용, 현재 노드)

    while q:
        # 1. 힙에서 뺀다
        cost, now = heapq.heappop(q)
        # 전략 1. cost가 reusult보다 크면 continue
        if result[now] < cost: continue

        # 2. 다음 갈 곳 예약(힙에 넣기)
        for i in range(A):
            if arr[now][i] == 0: continue
            next_cost = arr[now][i]
            cost_sum = cost + next_cost

            # 전략 2. cost_sum이 result보다 작으면 값 갱신
            if result[i] > cost_sum:
                result[i] = cost_sum
                heapq.heappush(q, (cost_sum, i))
    # 도착 노드까지 최소 값 반환
    return result[end_node]


# main
T = int(input())
for tc in range(1, T+1):
    # N: 목표지점, E: 도로 개수
    N, E = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(E):
        # 시작노드, 끝 노드, 구간 거리
        s, e, w = map(int, input().split())
        arr[s][e] = w

    answer = dijkstra(N)
    print(f'#{tc} {answer}')
