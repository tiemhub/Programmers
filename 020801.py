"""
스택을 활용하는 문제처럼 보임
110 찾기 and 마지막 0 찾기

110 탐색 -> 110 앞에 위치하는 마지막 0 뒤에 삽입
계속 반복
"""


def changNum(num,flag,flag0):
    return num[:flag0] + '110' + num[flag0:flag] + num[flag+3:]

def findNum(num: int):
    flag = 0
    flag0 = -1
    while flag < (len(num)-2):
        print(num,flag,flag0)
        if num[flag:flag+3] == '110':
            num = changNum(num,flag,flag0+1)
            flag = flag0+2
            flag0 = flag
        elif num[flag] == '0':
            flag0 = flag
        flag += 1
    
    return num

num = input()
print(findNum(num))