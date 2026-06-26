n,k=map(int, input().split())
def wabbits(n,k):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return wabbits(n-1, k) + k*wabbits(n-2, k)
print(wabbits(n,k))
