N, M = input('Введите через пробел количество мест и часов: ').split()
N = int(N)
M = int(M)
Cn = [0]*N

print('Введите через Enter количество печенек в каждом месте:')
for i in range(len(Cn)):
    Cn[i] = int(input())

def search(n, m, cn):
    if m < n:
        return 0
    if n == n:
        return max(cn)

print(search(N, M, Cn))




