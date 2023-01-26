import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0] # 누적합을 저장할 배열 -> 인덱스를 편리하게 하기 위해 [0] 넣고 시작
sum = 0 # 누적합을 저장할 변수

for num in nums:
    sum += num  
    prefix_sum.append(sum) # 각 값들을 더해 배열에 넣어줌

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
    