import sys
input = sys.stdin.readline

N = int(input())
answer = []

for i in range(1, N+1):
    
    i = str(i)
    clap = i.count('3') + i.count('6') + i.count('9')

    if clap == 0:
        answer.append(i)
    else:
        answer.append("-" * clap)

print(*answer)