in_file = open('buckets.in')
out_file = open('buckets.out', 'w')

L = 0j  # Lake
B = 0j  # Barn
R = set()  # Rocks
# Walls to prevent cows from going outside
for i in range(10):
    R |= {i*1j - 1, i*1j + 10, -1j + i, 10j + i}
# Read input
for y in range(10):
    line = in_file.readline().strip()
    for x, char in enumerate(line):
        pos = x + 1j * y
        if char == 'R':
            R.add(pos)
        elif char == 'L':
            L = pos
        elif char == 'B':
            B = pos

# Standard bfs
seen = {B}
steps = 0
while L not in seen:
    for pos in seen.copy():
        for delta in (1, -1, 1j, -1j):
            seen.add(pos + delta)
    seen -= R
    steps += 1

print(steps - 1, file=out_file)
