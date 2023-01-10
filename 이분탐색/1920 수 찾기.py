# 이분탐색 이용

n = int(input())
nlist = list(map(str, input().split()))
m = int(input())
mlist = list(map(str, input().split()))

nlist.sort()

def binary(i):
    first = 0
    last = n - 1
    
    while first <= last:
        mid = (first + last) // 2
        if nlist[mid] == i:
            return True
        
        elif i > nlist[mid]:
            first = mid + 1
        
        elif i < nlist[mid]:
            last = mid - 1

for i in range(m):
    if binary(mlist[i]): #True라면
        print(1)
    else:
        print(0)