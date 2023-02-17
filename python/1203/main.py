N = int(input())

for _ in range(N):
    n = int(input())
    counts = list(map(int, input().split()))
    total = sum(counts)
    for target_count in range(n, 0, -1):
        target_sum, remainder = divmod(total, target_count)
        if remainder != 0:
            continue
        current_sum = 0
        for c in counts:
            current_sum += c
            if current_sum > target_sum:
                break
            elif current_sum == target_sum:
                current_sum = 0
        else:
            print(n - target_count)
            break
