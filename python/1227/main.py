input()  # Ignore first line

cows = [i == 'G' for i in input()]  # G is true, H is false
# Group into pairs. HH/GG can be ignored
# HG -> True (OK) and GH -> False (Needs to be swapped)
pairs = [j == 1 for i, j in zip(*[iter(cows)]*2) if i != j]
pairs.append(True)  # have to make everything True at the end

# Find number of times the state has to be switched
current = pairs[0]
t = 0
for i in pairs:
    if i != current:
        t += 1
        current = i


print(t)
