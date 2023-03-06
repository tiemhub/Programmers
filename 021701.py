"""
110 옮기기
새로운 방식
문자열을 순회하며 원 문자열을 가공하는 것이 아닌 새로운 문자열을 생성

"""
def findNum(num):
    substr = ''
    cnt = 0

    #숫자를 순회하며 110의 개수를 세고 새로운 문자열 생성
    for n in num:
        print(num,n,substr,cnt)
        if n == '0':
            if (len(substr) > 1) and substr[-2:] == '11':
                    substr = substr[:-2]
                    cnt += 1
            else:
                substr += '0'
        else:
            substr += '1'
    print(num,n,substr,cnt)
    #새로운 문자열을 순회하며 110 삽입할 위치를 확인
    
    flag = 0
    flag0 = -1
    doubled = False

    for i in range(len(substr)):
        if substr[i] == '1':
            if doubled:
                flag = max(0,i-1)
                break
            else:
                doubled = True
        else:
            flag0 = i
            double = False
        print(flag,flag0,doubled)
    else:
        if flag0 != -1:
            flag = flag0+1
        else:
            flag = 0

    ans = substr[:flag] + '110'*cnt + substr[flag:]
    return ans

num = input()
print(findNum(num))
    