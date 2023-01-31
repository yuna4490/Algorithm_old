# 이건 통과한 듯

def solution(price, money, count):
    answer = -1
    prices = 0
    
    for i in range(count):
        prices += price * (i+1)
        print(prices)
    
    if prices > money:
        answer = prices - money
    
    else:
        answer = 0
    
    return answer