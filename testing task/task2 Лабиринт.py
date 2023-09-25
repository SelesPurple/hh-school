from collections import deque

N, M = map(int, input().split())
y1, x1 = map(int, input().split())
y2, x2 = map(int, input().split())
grid = [[*map(int, input().split())] for i in range(N)]
# другой способ задать кортеж a, b = (int(x) for x in input().split())

dist = [[-1] * M for i in range(N)]
q = deque()
q.append((x1, y1))
dist[x1][y1] = 0


while q:
    tx, ty = q.popleft()
    if tx == x2 and ty == y2:
        print(dist[x2][y2])
        break
    for dx, dy in [(0, 1), (1, 0), (0, -1,), (-1, 0)]:
        xn = tx + dx
        yn = ty + dy
        if (0 <= xn < N) and (0 <= yn < M) and (grid[xn][yn] == 0) and (dist[xn][yn] == -1):
            dist[xn][yn] = dist[tx][ty] + 1
            q.append((xn, yn))
else:
    print(0)
