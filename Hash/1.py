#코딩테스트 - 해쉬
#완주하지 못한 사람

def solution(participant, completion): 
    hash ={} 
    for i in participant: 
        if i in hash: 
            hash[i] += 1 
        else: 
            hash[i] = 1 
    for i in completion: 
        if hash[i] == 1: 
            del hash[i] 
        else: 
            hash[i] -= 1 
    answer = list(hash.keys())[0] 
    return answer #성공
