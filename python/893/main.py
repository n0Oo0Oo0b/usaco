import itertools

in_file = open('guess.in')
out_file = open('guess.out', 'w')

N = int(in_file.readline())

animals = []
for _ in range(N):
    _, _, *c = in_file.readline().split()
    animals.append(set(c))

m = 0
for i, j in itertools.combinations(animals, 2):
    m = max(m, len(i & j))

print(m+1, file=out_file)
