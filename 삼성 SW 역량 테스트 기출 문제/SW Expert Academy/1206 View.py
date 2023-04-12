import sys
input = sys.stdin.readline

for i in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0

    for i in range(2, N-2):
        if buildings[i] > buildings[i-1] and buildings[i] > buildings[i+1] and buildings[i] > buildings[i-2] and buildings[i] > buildings[i+2]:
            cnt += min(buildings[i] - buildings[i-1], buildings[i] - buildings[i+1], buildings[i] - buildings[i-2], buildings[i] - buildings[i+2])
    
    print('#' + str(i), cnt)