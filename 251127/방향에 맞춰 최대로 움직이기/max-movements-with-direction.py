n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

# 방향 매핑 (문제에서 주어진 1~8 방향 정의)
dr = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 0, 1, 1, 1, 0, -1, -1, -1]

# 다음에 이동할 수 있는 칸을 미리 저장 (메모리 2D 리스트)
next_pos = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        d = move_dir[i][j]  # 현재 칸의 방향
        nr, nc = i + dr[d], j + dc[d]

        # 같은 방향으로 계속 진행
        while 0 <= nr < n and 0 <= nc < n:
            # 조건: 수가 더 큰 칸만 이동 가능
            if num[nr][nc] > num[i][j]:
                next_pos[i][j].append((nr, nc))
            nr += dr[d]
            nc += dc[d]

# DFS + DP (메모이제이션)
dp = [[-1] * n for _ in range(n)]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    max_steps = 0
    for nx, ny in next_pos[x][y]:
        max_steps = max(max_steps, 1 + dfs(nx, ny))

    dp[x][y] = max_steps
    return dp[x][y]

print(dfs(r, c))
