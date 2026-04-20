n, m = map(int, input().split())
sex = list(input().split())
univ = []
boss = [i for i in range(10)]
cost = 0
cnt = 0

for _ in range(m):
    u, v, d = map(int, input().split())
    univ.append((d, u, v))
univ.sort() # d를 기준으로 오름차순 정렬

def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)
    if a == b: return
    boss[b] = a


def Find(n):
    if boss[n] == n:
        return n
    result = Find(boss[n])
    boss[n] = result
    return result

for d, u, v in univ:
    if Find(u) == Find(v):
        continue
    if sex[u-1] == sex[v-1]: # 인덱스
        continue
    Union(u,v)
    cnt += 1
    cost += d
if cnt != n-1: # 노드개수-1이 아니면 모든 학교 연결 못한 것
    print(-1)
else: print(cost)

