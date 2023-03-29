def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        x = ""
        for s in skill_tree:
            if s in skill:
                x += s
        
        if skill[0:len(x)] == x:
            answer += 1
        
    return answer