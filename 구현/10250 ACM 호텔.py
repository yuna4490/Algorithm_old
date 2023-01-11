t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    room = ''
    cnt = 0
    for i in range(w):
        for j in range(h):
            cnt += 1
            if cnt == n:
                if i+1 >= 10:
                    room = str(j+1) + str(i+1)
                
                else:
                    room = str(j+1) + '0' + str(i+1)
    
    print(room)