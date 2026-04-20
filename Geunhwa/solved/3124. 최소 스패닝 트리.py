T = int(input()) # 테스트케이스 수

for tc in range(1, T+1):
    V, E = map(int, input().split()) # 정점의 개수, 간선의 개수

    graph = []
    for _ in range(E):
        # A, B가 가중치 C인 간선으로 연결됨
        A, B, C = map(int, input().split())
        graph.append((C, A, B))

    # 간선 길이순(c기준) 정렬
    graph.sort()

    # union-find
    parent = [i for i in range(V+1)]

    def Find(i):
        # 자기가 부모일 경우, 자기를 리턴
        if parent[i] == i:
            return i

        f = Find(parent[i])
        parent[i] = f # 시간 단축

        return f

    def Union(a, b):
        parentA = Find(a)
        parentB = Find(b)

        if parentA == parentB: return
        else: parent[parentB] = parentA

    ans = 0 # 가중치의 합
    for c, a, b in graph:
        # 이미 연결되어 있다면 제외
        if Find(a) == Find(b): continue
        Union(a, b)
        ans += c


    # 답 출력
    print(f'#{tc} {ans}')

