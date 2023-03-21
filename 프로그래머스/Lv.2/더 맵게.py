import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville:
        
        if scoville[0] >= K:
            return answer
            
        if len(scoville) > 1 and scoville[0] < K:
            x = heapq.heappop(scoville)
            y = heapq.heappop(scoville)
            
            heapq.heappush(scoville, x + y*2)
            answer += 1
        
        elif len(scoville) == 1 and scoville[0] < K:
            return -1
    