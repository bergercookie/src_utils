def bisect_left(level_strengths, one_player):

    for param in range(N):
        x = one_player[param]
        lo = 0
        hi = len(level_strengths[param])
        while lo < hi:
            mid = (lo+hi)//2
            if level_strengths[param][mid] <= x: lo = mid+1
            else: hi = mid
        yield lo

# Initialization
[N, M, Q] = [int(i) for i in raw_input().split()] # Do not use ' ' !!!
level_strengths = [[0] * M ] * N
players_strengths = [[0] * N ] * Q
for param in range(N):
    level_strengths[param] = [int(i) for i in raw_input().split()] 
for query in range(Q):
    players_strengths[query] = [int(i) for i in raw_input().split()] 

for query in range(Q):
    decide_levels = bisect_left(level_strengths, players_strengths[query])
    print min(decide_levels)
