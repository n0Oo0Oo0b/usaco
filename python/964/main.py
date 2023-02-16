in_file = open('whereami.in')
out_file = open('whereami.out', 'w')


def check(k):
    seen = set()
    for i in range(len(data)-k+1):
        region = data[i:i+k]
        if region in seen:
            return False
        seen.add(region)
    return True


N = int(in_file.readline())
data = tuple(in_file.readline().strip())

print(next(filter(check, range(2, N+1))), file=out_file)
