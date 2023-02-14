import itertools

inp_file = open('race.in')
out_file = open('race.out', 'w')

K, N = map(int, inp_file.readline().split())


for _ in range(N):
    x = int(inp_file.readline())
    if x * (x + 1) // 2 >= K:  # Can reach finish by just accelerating
        # 1+2+3+...+v >= K
        # v*(v+1)/2 >= K
        # v*(v+1) >= K*2
        # v**2 + v >= K*2
        # v is approximately sqrt(K*2) -> check the integer values around it
        v = int((K*2)**0.5)  # int() truncates decimal points
        res = v + (v*(v+1) >= K*2)  # add extra if needed
    else:  # Have to decelerate
        # Add the additional distance if we decelerated till 0 to make it symmetrical
        s = K + (x * (x - 1) // 2)
        # either 1 + 2 + ... + v-1 + v + v-1 + ... + 2 + 1
        #   = 2 * (1 + 2 + ... + v-1) + v
        #   = 2 * ((v-1) * v / 2) + v
        #   = (v-1) * v + v
        #   = v * v
        # or 1 + 2 + ... + v-1 + v + v + v-1 + ... + 2 + 1  (note double v)
        # since option 1 is always smaller, solve the first case and see if the extra v is needed
        v = int(s**0.5)
        res = v*2 - x + 1  # time to accelerate to v and decelerate back to x
        res += (v*(v+1) < s)  # add extra if needed
    print(res, file=out_file)
