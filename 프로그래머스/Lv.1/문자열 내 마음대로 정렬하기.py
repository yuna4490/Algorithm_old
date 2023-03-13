# 내 풀이
def solution(strings, n):
    answer = []
    dic = dict()
    
    for string in strings:
        x = string[n]
        if dic.get(x) == None:
            dic[x] = list()
            dic[x].append(string)
        
        else:
            dic[x].append(string)
    
    for key in dic.keys():
        dic[key].sort()
    
    dic = dict(sorted(dic.items()))
    
    for key in dic.keys():
        for i in dic[key]:
            answer.append(i)
    
    return answer

# 더 효율적인 풀이
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])