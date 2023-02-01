def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        idx = []
        flag = 0
        for i in skill:
            if i in skill_tree:
                idx.append(skill_tree.index(i))
            else:
                idx.append(27)
        
        for j in range(0, len(idx)-1):
            
            if idx[j] > idx[j+1]:
                flag = 1
                break
            
        if flag == 0:
            answer += 1

    return answer