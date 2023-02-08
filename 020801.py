"""
스택을 활용하는 문제처럼 보임
110 찾기 and 마지막 0 찾기

110 탐색 -> 110 앞에 위치하는 마지막 0 뒤에 삽입
계속 반복
"""


def findNum(num: int):
    flag = 0
    for i in range(len(num)):
        if num[i:i+3] == '110':
            if flag == 0:
                pass
            else:
                
