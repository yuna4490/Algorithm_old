import heapq

def solution(operations):
    answer = []
    heap = []
    
    for operation in operations: 
        if operation[0] == 'I':
            heapq.heappush(heap, int(operation[2:]))
        
        else:
            if not heap:
                continue
            
            if operation[2] == '-':
                heapq.heappop(heap)
            
            else:
                heap = heapq.nlargest(len(heap), heap)[1:] # 힙에서 최댓값 제외
                heapq.heapify(heap) # 다시 최소 힙으로 되돌리기
    
    if not heap:
        answer.append(0)
        answer.append(0)
    
    else:
        answer.append(max(heap))
        answer.append(min(heap))
    
    return answer