def Find(x):
    if boss[x] == x: return x
    boss[x] = Find(boss[x])
    return boss[x]

def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)
    if a == b: return
    boss[b] = a

# main
t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())

    boss = [i for i in range(v + 1)]
    edges = []
    for _ in range(e):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    edges.sort()
    total = 0
    cnt = 0

    for cost, a, b in edges:
        if Find(a) == Find(b): continue
        Union(a, b)
        total += cost
        cnt += 1
        if cnt == v: break

    print(f'#{tc} {total}')
