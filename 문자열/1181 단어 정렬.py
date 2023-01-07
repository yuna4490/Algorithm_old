n = int(input())
arr = [input() for _ in range(n)]

arr.sort() # 하위 조건 먼저 정렬
arr.sort(key = len) # 상위 조건 그다음 정렬

arr = set(arr)
for i in arr:
    print(i)
    
