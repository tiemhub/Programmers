"""
스택을 활용하는 문제처럼 보임
110 찾기 and 마지막 0 찾기

110 탐색 -> 110 앞에 위치하는 마지막 0 뒤에 삽입
계속 반복
"""


# def changNum(num,flag,flag0):
#     return num[:flag0] + '110' + num[flag0:flag] + num[flag+3:]

# def findNum(num: int):
#     flag = 0
#     flag0 = -1
#     while flag < (len(num)-2):
#         print(num,flag,flag0)
#         if num[flag:flag+3] == '110':
#             num = changNum(num,flag,flag0+1)
#             flag = flag0+2
#             flag0 = flag
#         elif num[flag] == '0':
#             flag0 = flag
#         flag += 1
    
#     return num


def findNum(num: int):

    #문자열을 돌면서 110을 찾고 제거하는 작업
    flag = 0
    cnt = 0
    while flag < (len(num)-2):
        if num[flag:flag+3] == '110':
            cnt += 1
            num = num[:flag] + num[flag+3:]
            flag = max(0,flag-3)
        flag += 1

    #문자열을 돌면서 적절한 위치를 찾아 cnt만큼 110을 삽입
    # 1. 연속되 11 앞에 삽입 -> 가장 정석적이나 예외 처리가 필요함
    # 길이가 1일 때, 0이면 1, 1이면 0
    # 길이가 2일 때, 00이면 2, 10이면 2, 01이면 1, 11이면 0
    # 길이가 3일 때, 000이면 3, 001이면 2, 010이면 3, 011이면 1, 100이면 3, 
    flag = 0
    flag0 = -1
    doubled = False
    while flag < len(num)-1:
        if num[flag] == '1':
            if doubled:
                flag = max(0,flag-1)
                break
            else:
                doubled = True
        else:
            flag0 = flag
        flag += 1
    else:
        if flag0 == -1:
            pass
        else:
            flag = flag0
    
    if num == '1':
        flag = 0
    
    num = num[:flag] + '110'*cnt + num[flag:]
    return num



num = input()
print(findNum(num))