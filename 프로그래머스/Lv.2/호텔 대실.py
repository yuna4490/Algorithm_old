def solution(book_time):
    rooms = []
    book_times = sorted([[int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])] for s, e in book_time])
    
    for s, e in book_times:
        flag = 0
            
        for i, room in enumerate(rooms):
            if room <= s:
                rooms[i] = e + 10
                flag = 1
                break
        
        if flag == 0:
            rooms.append(e + 10)
        
    return len(rooms)