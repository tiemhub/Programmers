"""
사라지는 발판

승자 패자는 이미 정해짐 -> 누가 잡히냐 보다는 게임이 끝나지 않는 선에서 얼마나 많은 이동을 하느냐가 중점

bfs로 최댓값을 탐색?
visited 배열을 만들어서 사용할 필요성

"""

def solution(board, aloc, bloc):
    answer = -1
    
    visited = [False for _ in range(len(board[0]))]*len(board)
    
    return answer