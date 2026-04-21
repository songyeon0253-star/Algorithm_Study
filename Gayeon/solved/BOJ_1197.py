import sys
input = sys.stdin.readline

def Find(x):
    while boss[x] != x:
        boss[x] = boss[boss[x]]
        x = boss[x]
    return x

def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)
    if a == b: return
    boss[b] = a

# main
v, e = map(int, input().split())
boss = [i for i in range(v+1)]
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
    if cnt == v-1: break

print(total)