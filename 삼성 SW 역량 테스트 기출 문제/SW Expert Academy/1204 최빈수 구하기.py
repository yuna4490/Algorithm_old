#1 딕셔너리 활용
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    scores = list(map(int, input().split()))

    dic = defaultdict(int)

    for score in scores:
        dic[score] += 1
    
    dic = sorted(dic.items(), key = lambda x : (-x[1], -x[0]))
    print('#' + str(N), dic[0][0])



from collections import Counter


#2 Counter 활용
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    
    c = Counter(scores)
    c_list = sorted(c.items(), key = lambda x : (-x[1], -x[0]))
    
    print('#' + str(N), c_list[0][0])