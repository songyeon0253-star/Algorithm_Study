N, M = map(int, input().split()) # 학교의 수, 도로의 개수
mw = [''] + input().split() # 남여 대학 정보

graph = []
for _ in range(M):
    u, v, d = map(int, input().split()) # u학교와 v학교의 거리는 d

    # 동성 대학간의 경로일 경우 제외
    if mw[u] == mw[v]: continue

    graph.append((d, u, v))

# 거리순 정렬
graph.sort()

# 크루스칼
parent = [i for i in range(N+1)]

def Find(i):
    if parent[i] == i: return i

    parent[i] = Find(parent[i]) # 시간 단축
    return parent[i]

def Union(a, b):
    parentA = Find(a)
    parentB = Find(b)

    if parentA == parentB: return
    else:
        parent[b] = parentA
        return

ans = 0
connect = [False] * (N+1)
for d, u, v in graph:
    if Find(u) == Find(v): continue

    ans += d
    Union(u, v)
    connect[u] = True
    connect[v] = True

# 모든 학교를 연결했는지 확인
def is_route():
    for i in range(1, N+1):
        # 모든 학교를 연결하는 경로가 없는 경우
        if connect[i] == False:
            return -1

    return ans

print(is_route())
