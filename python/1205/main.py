from itertools import permutations, product

N = int(input())

cubes = [set(input()) for _ in range(4)]

possible = set()
for n_cubes in range(1, 5):
    for c in permutations(cubes, n_cubes):
        for p in product(*c):
            possible.add(''.join(p))

t = 0
for _ in range(N):
    if input() in possible:
        print('YES')
    else:
        print('NO')
