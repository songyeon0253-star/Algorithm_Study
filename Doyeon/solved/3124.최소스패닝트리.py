def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)
    if a == b:
        return
    boss[b] = a

def Find(n):
    if boss[n] == n:
        return n
    result = Find(boss[n])
    boss[n] = result
    return result


t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    boss = [i for i in range(v+1)] # a, b 가 1부터이므로 길이를 하나 더 길게
    tree = []
    cost = 0

    for _ in range(e):
        a, b, c = map(int, input().split())
        tree.append((c, a, b))
    tree.sort()
    for c, a, b in tree:
        if Find(a) == Find(b):
            continue
        Union(a, b)
        cost += c
    print(f'#{tc} {cost}')
