import collections
import functools

inp_file = open('factory.in')
out_file = open('factory.out', 'w')

N = int(inp_file.readline())
paths = collections.defaultdict(list)

for _ in range(N-1):
    a, b = map(int, inp_file.readline().split())
    paths[b].append(a)


@functools.lru_cache(maxsize=N)
def resolve(x):
    s = {x}
    for i in paths[x]:
        s |= resolve(i)
    return s


for i in range(1, N+1):
    if len(resolve(i)) == N:
        print(i, file=out_file)
        break
else:
    print(-1, file=out_file)
