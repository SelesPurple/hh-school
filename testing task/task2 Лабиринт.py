N, M = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
# Далее N строк, на каждой из которых M чисел 0 или 1 через пробел
grid = [0] * N
for i in range(M):
    grid[i] = [map(int, input().split())] * M
print(grid)