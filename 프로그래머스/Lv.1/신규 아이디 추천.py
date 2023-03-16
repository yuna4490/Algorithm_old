def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 1단계
    
    # 2단계
    for id in new_id:
        if id.isalnum() or id in '-_.':
            answer += id
    
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    # 4단계
    if len(answer) > 1 and answer[0] == '.':
        answer = answer[1:]
    
    if answer[-1] == '.': # 무조건 . 하나는 들어있음 아무것도 없을 수가 없음
        answer = answer[:-1]
    
    # 5단계
    if not len(answer):
        answer = "a"
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7단계
    if len(answer) <= 2:
        answer += answer[-1] * (3-len(answer))
    
    return answer