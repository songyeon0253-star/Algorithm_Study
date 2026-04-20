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
n, m = map(int, input().split())
WM = ['0'] + list(input().split())
boss = [i for i in range(n+1)]

universities = []
sum_c = 0
cnt = 0

for _ in range(m):
    u, v, cost = map(int, input().split())
    if WM[u] == WM[v]: continue
    universities.append((cost, u, v))

universities.sort()

for cost, u, v in universities:
    if Find(u) == Find(v): continue
    Union(u, v)
    cnt += 1
    sum_c += cost

if cnt == n - 1:
    print(sum_c)
else:
    print(-1)