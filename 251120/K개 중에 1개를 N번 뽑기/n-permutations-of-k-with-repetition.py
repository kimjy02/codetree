K, N = map(int, input().split())
def dfs(depth):
    if depth == N:
        print(*result)
        return
    for num in range(1, K+1):
        result[depth] = num
        dfs(depth + 1)

result = [0] * N

dfs(0)