K, N = map(int, input().split())

# Please write your code here.
def dfs(depth, path):
    if depth == N:
        print(*path)
        return

    for x in range(1, K+1):
        if len(path) >= 2 and path[-2] == x and path[-1] == x:
            continue

        path.append(x)
        dfs(depth + 1, path)
        path.pop()

dfs(0, [])