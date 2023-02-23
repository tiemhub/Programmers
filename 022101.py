"""
사라지는 발판

승자 패자는 이미 정해짐 -> 누가 잡히냐 보다는 게임이 끝나지 않는 선에서 얼마나 많은 이동을 하느냐가 중점

bfs로 최댓값을 탐색?
visited 배열을 만들어서 사용할 필요성

bfs 탐색하면서 a,b가 동시에 같은 발판에 경우의 수를 고려해야함
visited 데이터 갱신을 이동하는 즉시가 아닌, 이동 이후 자신이 있던 발판의 데이터를 바꾸는 식으로 구성

"""

def solution(board, aloc, bloc):
    answer = -1
    
    visited = [False for _ in range(len(board[0]))]*len(board)
    visited[aloc[0],aloc[1]] = True
    visited[bloc[0],bloc[1]] = True



    return answer