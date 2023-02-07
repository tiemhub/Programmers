"""
뒤집혀야 되는 지에 대한 여부를 새로운 배열로 만들고,
그 배열이 줄 계산을 통해 0배열로 변환이 가능한지
"""

def solution(beginning, target):
    answer = 0
    cnt = 0
    arr = [[0]*len(beginning[0]) for _ in range(len(beginning))]

    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            arr[i][j] = abs(beginning[i][j] - target[i][j])
    
    for i in range(len(beginning)):
        print(arr[i])

    standard = []
    for i in range(len(arr[0])):
        standard.append(abs(arr[0][i]-1))

    for i in range(1,len(arr)):
        if arr[0] == arr[i]:
            pass
        elif standard == arr[i]:
            cnt += 1
        else:
            return -1

    val1 = cnt + sum(arr[0])
    val2 = (len(arr)-cnt) + sum(standard)
    return min(val1,val2)


beginning = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
print(solution(beginning,target))