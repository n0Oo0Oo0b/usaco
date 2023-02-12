import itertools

in_file = open('gymnastics.in')
out_file = open('gymnastics.out', 'w')

K, N = map(int, in_file.readline().split())

consistent_pairs = None

for _ in range(K):
    current = {*itertools.combinations(map(int, in_file.readline().split()), 2)}
    if consistent_pairs is None:
        consistent_pairs = current
    else:
        consistent_pairs &= current

print(len(consistent_pairs), file=out_file)
