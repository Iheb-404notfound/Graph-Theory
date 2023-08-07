# Variables
inf = float('inf')
graph = [  
    #  0    1    2    3    4    5    6    7   8   9     10
    [  0,   0,   0,  -4,   0,   0,   0,   0,  0,   0,   0], # 0
    [ -3,   0,   8,   0,   0,   0,   0,   0,  0,   0,   0], # 1
    [  0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0], # 2
    [  0,   0,   0,   0,   0,   0,   0,   0,  0,  10,   0], # 3
    [  0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0], # 4
    [  0,   0,   0,   0,   0,   0,   0,   0,  0,   1,   9], # 5
    [  0,   0,   0,   0,   0,   2,   0,   0,  0,   0,   0], # 6
    [  0,   0,  -9,   0,   0,   0,   0,   0,  0,  10,   5], # 7
    [ 10,   4,   0,   0,   0,   0,   0,   5,  0,   0,   0], # 8
    [  0,   0,   0,   0,   0,   0,   0,   0,  5,   0,   0], # 9
    [  0,   0,   0,   0,   0,   0,   8,   0,  0,   0,   0], # 10
]

def show(g):
    for l in g:
        for c in l:
            r = '-∞'
            if c ==inf:
                r = '+∞'
            elif not c==-inf:
                r = f'{c:02d}'
            print(r, end=' ')
        print()
    print()

#APSP Floyd-Warshall Algorithm
def fw(graph):
    n = len(graph)
    r = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if not graph[i][j] == 0:
                r[i][j] = graph[i][j]
    # The Actual Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                r[i][j] = min(r[i][k] + r[k][j], r[i][j])

    # Detect negative cycles
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if r[i][j] > r[i][k] + r[k][j]:
                    r[i][j] = -inf
    return r

show(fw(graph))