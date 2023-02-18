N = int(input())

# Split cows into L and G
L = []
G = []
for _ in range(N):
    a, b = input().split()
    b = int(b)
    if a == 'L':
        L.append(b)
    else:
        G.append(b)

m = 1000
for pos in min(set(G), set(L), key=len):  # iterate over shorter one
    t = N  # assume all cows are lying
    for i in G:
        if pos >= i:
            t -= 1  # cow is not lying
    for i in L:
        if pos <= i:
            t -= 1  # cow is not lying
    m = min(m, t)

if L and G:
    print(m)
else:
    print(0)  # either list is empty
