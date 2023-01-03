# isalpha() : 문자열이 영어나 한글로 되어 있으면 참 리턴
# isalnum() : 문자열이 영어, 한글 혹은 숫자로 되어 있으면 참 리턴
import sys
input = sys.stdin.readline

string = list(input().rstrip())

i = 0
while i < len(string):
    if string[i] == '<': # '<'가 오면 그냥 pass
        i += 1
        while string[i] != '>': # '>'가 올때까지 그냥 pass
            i += 1
        i += 1 # string[i] == '>' 일 때도 pass

    elif string[i].isalnum():
        start = i
        while i < len(string) and string[i].isalnum():
            i += 1
        tmp = string[start:i]
        tmp.reverse() # 뒤집기
        string[start:i] = tmp

    else:
        i += 1 # 공백이 나올 경우 그냥 증가

print(''.join(string))    
    





