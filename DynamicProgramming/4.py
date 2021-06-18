def solution(money):
    answer = 0
    s1, s2 = 0, 0
    r1, r2 = 0, 0

    first = True
    
    for i in money:
        r1, r2 = r2, max(r1+i,r2)
        
    
    return max(r1,r2)

print(solution(list(map(int,input().split()))))
