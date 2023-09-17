N, M = input().split()
N = int(N)
M = int(M)
Cn = [0]*N

for i in range(len(Cn)):
    Cn[i] = int(input())
def search(n, m, cn):
    for c in cn:
        if c == 0:
            cn.remove(c)
            n =- 1
    if m < n:
        return 0
    low = 1
    high = max(cn)
    while low < high:
        mid = (high + low) // 2
        temp_sum = 0
        for c in cn:
            temp_sum += (c + mid - 1) // mid
        if temp_sum > m:
            low = mid + 1
        else:
            high = mid
    return low

print(search(N, M, Cn))




