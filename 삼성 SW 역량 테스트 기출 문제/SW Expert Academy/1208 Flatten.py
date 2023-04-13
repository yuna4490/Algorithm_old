import sys
input = sys.stdin.readline

for i in range(1, 11):
    N = int(input()) # 주어진 덤프 횟수
    
    boxes = list(map(int, input().split()))

    while N > 0:

        N -= 1
        if max(boxes) - min(boxes) == 1:
            break

        max_idx = boxes.index(max(boxes))
        min_idx = boxes.index(min(boxes))

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    print('#' + str(i), max(boxes) - min(boxes))