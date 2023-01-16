n, k = map(int, input().split())
arr = list(input())
cnt = 0

for i in range(len(arr)):
    if arr[i] == 'P':
        for j in range(i-k, i+k+1):
            if j < 0 or j > n-1:
                continue

            elif arr[j] == 'H':
                cnt += 1
                arr[j] = 'A'
                break
                #부품 하나만 집고 넘어가
                
print(cnt)