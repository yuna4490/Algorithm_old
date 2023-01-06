import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = 0

nlist = [list(map(int, input().split())) for _ in range(n)]
mlist = [list(map(int, input().split())) for _ in range(m)]

while True:
    if not nlist or not mlist:
        break

    diff = mlist[0][0] - nlist[0][0] # 구간의 거리 차

    if diff > 0: # m > n 
        result = max(result, mlist[0][1] - nlist[0][1])
        mlist[0][0] -= nlist[0][0]
        nlist.pop(0)

    elif diff < 0: # m < n
        result = max(result, mlist[0][1] - nlist[0][1])
        nlist[0][0] -= mlist[0][0]
        mlist.pop(0)

    else:
        result = max(result, mlist[0][1] - nlist[0][1])
        nlist.pop(0)
        mlist.pop(0)

if result > 0:
    print(result)

else:
    print(0)