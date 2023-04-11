def solution(numbers, hand):
    answer = ''
    
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}

    lefthand = keypad['*']
    righthand = keypad['#']
    
    for number in numbers:
        now = keypad[number]
        
        if number in [1,4,7]:
            answer += 'L'
            lefthand = now
        
        elif number in [3,6,9]:
            answer += 'R'
            righthand = now
        
        else:
            tmp_left, tmp_right = 0, 0
            
            for num, a, b in zip(now, lefthand, righthand):
                tmp_left += abs(num - a)
                tmp_right += abs(num - b)
            
            if tmp_left > tmp_right:
                answer += 'R'
                righthand = now
            
            elif tmp_left < tmp_right:
                answer += 'L'
                lefthand = now
                
            else:
                if hand == 'right':
                    answer += 'R'
                    righthand = now
                else:
                    answer += 'L'
                    lefthand = now
                    
    return answer