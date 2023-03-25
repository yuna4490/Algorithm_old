def solution(dirs):
    
    d = {'U' : [0, 1], 'D' : [0, -1], 'L' : [-1, 0], 'R' : [1, 0]}
    
    visited = set()
    x, y = 0, 0
    
    for dir in dirs:
        nx = x + d[dir][0]
        ny = y + d[dir][1]
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x, y = nx, ny
            
    return len(visited)//2