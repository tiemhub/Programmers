def solution(m, n, puddles):
    
    li = [[0]*m for _ in range(n)]
    li[0][0] = 1
    
    for x,y in puddles:
        li[y-1][x-1] = -1
    
    for i in range(n):
        for j in range(m):
            if li[i][j] != -1:
                if i != n-1:
                    if li[i+1][j] != -1:
                        li[i+1][j] += li[i][j]
                if j != m-1:
                    if li[i][j+1] != -1:
                        li[i][j+1] += li[i][j]
    
    return li[-1][-1]
