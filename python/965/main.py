import itertools

cows = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']

inp_file = open('lineup.in')
out_file = open('lineup.out', 'w')

restraints = []
for _ in range(int(inp_file.readline())):
    a, *_, b = inp_file.readline().split()
    restraints.append((a, b))

for i in itertools.permutations(cows):
    for a, b in restraints:
        if abs(i.index(a) - i.index(b)) != 1:
            break
    else:
        for j in i:
            print(j, file=out_file)
        break
