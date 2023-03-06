"""
사라지는 발판

승자 패자는 이미 정해짐 -> 누가 잡히냐 보다는 게임이 끝나지 않는 선에서 얼마나 많은 이동을 하느냐가 중점

bfs로 최댓값을 탐색?
visited 배열을 만들어서 사용할 필요성

bfs 탐색하면서 a,b가 동시에 같은 발판에 경우의 수를 고려해야함
visited 데이터 갱신을 이동하는 즉시가 아닌, 이동 이후 자신이 있던 발판의 데이터를 바꾸는 식으로 구성

"""

def bfs(board, aloc, bloc, turn, cnt, val):
    #실패조건이 있는가
    #(이동가능&같은위치) | 이동불가
    if aloc == bloc: #같은 위치 판정을 위한 변수
        isSameLoc = True
    else:
        isSameLoc = False
    canMove = False #이동했는지의 여부를 통해 이동불가를 판정

    #탐색
    dxs = [0,1,0,-1]
    dys = [1,0,-1,0]
    if turn == 0:
        for dx in dxs:
            for dy in dys:
                if board[aloc[0]+dy][aloc[1]+dx] == 1:
                    if isSameLoc:
                        return (cnt+1)
                    board[aloc[0]][aloc[1]] == 0 #이동했으므로 발판 삭제
                    val = max(val,bfs(board, [aloc[0]+dy,aloc[1]+dx],bloc,1,cnt+1))
                    board[aloc[0]][aloc[1]] == 1
                    canMove = True
    else:
        for dx in dxs:
            for dy in dys:
                if board[bloc[0]+dy][bloc[1]+dx] == 1:
                    if isSameLoc:
                        return (cnt+1)
                    board[bloc[0]][bloc[1]] == 0 #이동했으므로 발판 삭제
                    val = max(val,bfs(board, aloc,[bloc[0]+dy,bloc[1]+dx],1,cnt+1))
                    board[bloc[0]][bloc[1]] == 1
                    canMove = True
    
    if not canMove: #이번 탐색에서 움직이지 못했다면 종료
        return cnt
    #탐색 완료&실패조건x -> val 유지
    return val


def solution(board, aloc, bloc):
    answer = -1
    
    answer = bfs(board,aloc,bloc,0,0,-1)

    return answer