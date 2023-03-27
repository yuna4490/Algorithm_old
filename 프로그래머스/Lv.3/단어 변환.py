from collections import deque

def solution(begin, target, words):
    answer = 0
    
    queue = deque()
    queue.append((begin, 0))
    visited = [0] * len(words)
    
    while queue:
        x, cnt = queue.popleft()
        
        if x == target:
            answer = cnt
            return answer
        
        for i in range(len(words)):
            count = 0
            for j in range(len(words[i])):
                if words[i][j] != x[j]:
                    count += 1
            
            if count == 1:
                queue.append((words[i], cnt+1))
                visited[i] = 1
        
    return answer