def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        
        tmp = tmp[2:].zfill(n) 
        # 2부터 자르고 n자리 수에 맞게 앞을 0으로 채워줌
        # zfill(자리수) => 앞을 0으로 채워줌
        # rjust(자리수, 원하는 문자) => 앞을 원하는 문자로 채워줌
        
        tmp = tmp.replace('1', '#').replace('0', ' ')
        
        answer.append(tmp)
    
    return answer