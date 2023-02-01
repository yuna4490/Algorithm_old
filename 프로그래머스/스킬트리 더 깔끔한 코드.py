def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_list = ''
        for i in skill_tree:
            if i in skill:
                skill_list += i
        
        if skill[0:len(skill_list)] == skill_list:
            answer += 1
            
    return answer