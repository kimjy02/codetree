N = int(input())
x, y = map(int, input().split())

grid = [list(input().strip()) for _ in range(N)]
# Please write your code here.
i, j = x-1, y-1
move_dct = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

# 초기에는 무조건 오른쪽으로 이동
move_idx = 1
time = 0
visited = [[0] * N for _ in range(N)]
visited[i][j] = 1

# 사방이 벽인 경우 바로 코드 탈출
blocked = True
for d in range(4):
    di, dj = move_dct[d]
    ni, nj = i + di, j + dj
    if 0 <= ni < N and 0 <= nj < N:
        if grid[ni][nj] != "#":
            blocked = False
            break
if blocked:
    print(-1)
    exit()

# 메일 실행 코드
while True:
    di, dj = move_dct[move_idx]
    ni, nj = i+di, j+dj
    wall_i, wall_j = move_dct[(move_idx+1) % 4]
    wi, wj = ni + wall_i, nj + wall_j

    if 0 > ni or N <= ni or 0 > nj or N <= nj:
        time += 1
        break

    if 0 <= ni < N and 0 <= nj < N:
        if grid[ni][nj] == "#":
            # 반시계 회전
            move_idx = (4 + (move_idx -1)) % 4

        else:
            time += 1
            if 0 <= wi < N and 0 <= wj < N:
                if grid[wi][wj] == "#": # 전진 + 이동 방향 유지
                    if visited[ni][nj] == 1:
                        time = -1
                        break
                    visited[ni][nj] = 1
                    i, j = ni, nj

                else: # 전진 + 이동 방향 시계 90 회전 + 전진
                    time += 1 # 전진 했다치고 여기서 시간 늘려주기
                    move_idx = (move_idx+1)%4
                    change_i, change_j = move_dct[move_idx]
                    ni, nj = ni + change_i, nj + change_j
                    if visited[ni][nj] == 1:
                        time = -1
                        break
                    visited[ni][nj] = 1
                    i, j = ni, nj

print(time)