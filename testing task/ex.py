def solve(n, m, arr):
    if m < n or n == 0:
        return 0
    lo = 1
    hi = max(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if sum((c + mid - 1) // mid for c in arr) <= m:
            hi = mid
        else:
            lo = mid + 1

    return lo


n, m = map(int, input().split())
cookies = [int(input()) for _ in range(n)]
cookies = [x for x in cookies if x > 0]
n = len(cookies)
print(solve(n, m, cookies))