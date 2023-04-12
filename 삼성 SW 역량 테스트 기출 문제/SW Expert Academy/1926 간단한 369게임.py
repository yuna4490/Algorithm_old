import sys
input = sys.stdin.readline

N = int(input())
answer = []

for i in range(1, N+1):
    clap = ''
    if '3' in str(i):
        for _ in range(str(i).count('3')):
            clap += '-'
    
    if '6' in str(i):
        for _ in range(str(i).count('6')):
            clap += '-'
    
    if '9' in str(i):
        for _ in range(str(i).count('9')):
            clap += '-'
    
    if len(clap) == 0:
        answer.append(i)
    
    else:
        answer.append(clap)

print(*answer)