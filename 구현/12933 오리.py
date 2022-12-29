sound = input()
quack = "quack"
visited = [0] * len(sound)
cnt = 0

def find(start):
    global cnt
    j = 1
    first = True
    for i in range(start+1, len(sound)):
        if sound[i] == quack[j] and not visited[i]:
            visited[i] = 1
            if sound[i] == 'k': # 마지막 문자
                if first: # 만약 처음 울음소리가 완성된 거라면
                    first = False
                    cnt += 1
                j = 1
            
            else:
                j += 1

if len(sound) % 5 != 0: # 5의 배수가 아니라면 올바르지 않은 소리
    print(-1)

for i in range(len(sound)):
    if sound[i] == 'q' and not visited[i]: # 방문하지 않은 q가 있으면
        find(i)

if cnt == 0 or not all(visited): # 오리가 0마리이거나 모든 문자를 방문하지 않았을 경우
    print(-1) # 올바르지 않은 소리

else:
    print(cnt)
