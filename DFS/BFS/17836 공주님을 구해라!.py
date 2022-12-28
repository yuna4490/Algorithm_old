from collections import deque

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, d):
    queue = deque()
    queue.append([i, j, d])
    visited[i][j] = 1

    result = 10001

    while queue:
        x, y, d = queue.popleft()

        if x == n-1 and y == m-1: # 공주가 있는 지점에 도착하면
            result = min(result, d) # 최소 시간 구함
            break

        if d+1 > t: # 현재 걸린 시간에 +1 했을 때 t를 넘어가면 멈춤
            break

        for k in range(4): # 상하좌우 이동
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny, d+1])

                elif graph[nx][ny] == 2: # 그람이 있다면
                    temp = d + 1 # 그람까지 온 거리
                    temp += abs(n-1 - nx) + abs(m-1 - ny)
                    visited[nx][ny] = 1

                    if temp <= t: # 이동 시간이 t와 같거나 작다면
                        result = temp
    
    return result


result = bfs(0,0,0)

if result == 10001:
    print("Fail")

else:
    print(result)
    