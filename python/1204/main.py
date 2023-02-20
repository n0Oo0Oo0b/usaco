input()

current = list(map(int, input().split()))
target = list(map(int, input().split()))
target_index = {j: i for i, j in enumerate(target)}

need_to_move = 0
highest_seen = 0
for index, item in enumerate(current):
    i = target_index[item]
    if i < highest_seen:
        need_to_move += 1
    highest_seen = max(highest_seen, i)

print(need_to_move)
