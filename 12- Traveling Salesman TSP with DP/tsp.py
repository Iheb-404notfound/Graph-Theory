#Variables and constants
adj_matrix = [
    [0, 2, 4, 6, 8],
    [2, 0, 3, 5, 7],
    [4, 3, 0, 1, 9],
    [6, 5, 1, 0, 4],
    [8, 7, 9, 4, 0]
]

INF = float('inf')

# This recursive method is used in the next function to create bit sets
def combinations(s, i, r, n, subs):
    if n - i < r: return
    if r == 0:
        subs.append(s)
    else:
        for j in range(i, n):
            s = s | 1<<j
            combinations(s, i+1, r-1, n, subs)
            s = s & ~(1<<j)
# returns all combinations of size N where there are r bits set to 1
# subsets(3, 4) = [0111, 1011, 1101, 1110]
def subsets(r, n):
    subs = []
    combinations(0, 0, r, n, subs)
    return subs

# ith bit in subset == 0 ?
def izero(i, subset):
    return ((1<<i) & subset) == 0

def tsp(graph, S):
    n = len(graph)
    # initialize table with null or -1 or +inf to prevent errors
    dp = [ [None] * (1<<n) for _ in range(n) ]
    # Catch the optimal solution from start node to others
    for i in range(n):
        if i == S: continue
        # Store the optimal value from node S to each node i
        dp[i][ 1<<S | 1<<i ] = graph[S][i]
    # solve
    for r in range(3, n+1):
        for subset in subsets(r, n):
            if izero(S, subset): continue
            for next in range(n):
                if next==S or izero(next, subset): continue
                #subset state without next node
                state = subset ^ (1<<next)
                minDist = INF
                for e in range(n):
                    if e == S or e == next or izero(e, subset): continue
                    minDist = min(dp[e][state] + graph[e][next], minDist)
                dp[next][subset] = minDist
    # Find minimum cost
    # the end state is the bit mask with n bits set to 1
    END_STATE = (1<<n)-1
    mc = INF
    for e in range(n):
        if e==S: continue
        mc = min(dp[e][END_STATE] + graph[e][S], mc)
    
    # Now Just find the optimal tour
    lastindex = S
    state = END_STATE
    tour = [S]
    for i in range(1, n):
        index = -1
        for j in range(n):
            if j==S or izero(j, state): continue
            if index==-1: index = j
            prev = dp[index][state] + graph[index][lastindex]
            new = dp[j][state] + graph[j][lastindex]
            if new < prev: index = j
        tour.append(index)
        state = state ^ (1<<index)
        lastindex = index
    tour.append(S)
    tour.reverse()
    return (mc, tour)

print(tsp(adj_matrix, 0))