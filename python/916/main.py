in_file = open('revegetate.in')
out_file = open('revegetate.out', 'w')

N, M = map(int, in_file.readline().split())

rules = [[] for _ in range(N)]
for _ in range(M):
    a, b = sorted(int(i) - 1 for i in in_file.readline().split())
    rules[b].append(a)

pastures = []

for i in range(N):
    n = set(pastures[j] for j in rules[i])
    next_ = min({1, 2, 3, 4} - n)
    pastures.append(next_)

print(*pastures, sep='', file=out_file)
