#같은 격자 2번 이상 방문 가능 -> visited를 구현 필요 x
#문자열이 제일 빠른순 -> 문자열 순서대로 bfs 탐색
#백트래킹?

def search(n,m,x,y,r,c,k):
    stack = [[(x,y),0,'']]
    
    while stack:
        print(stack)
        loc, dis, st = stack.pop(0)
        x,y = loc
           
        #현재 위치가 목적지와 같다면 문자열을 반환
        if (loc == (r,c)) and (dis == k):
            return st
        #거리가 k보다 크다면 탐색 실패이므로 종료
        if dis > k:
            return 'impossible'
        
        if x < n:
            stack.append([(x+1,y),dis+1,st+'d'])
        if y > 1:
            stack.append([(x,y-1),dis+1,st+'l'])
        if y < m:
            stack.append([(x,y+1),dis+1,st+'r'])
        if x > 1:
            stack.append([(x-1,y),dis+1,st+'u'])
    
    #while문이 종료 -> 탐색 실패 -> impossible
    return 'impossible'
        
        

n, m, x, y, r, c, k = map(int,input().split())
    
answer = search(n, m, x, y, r, c, k)
    
print(answer)