n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
from itertools import product
# Please write your code here.
bomb_dct = {
    1: [(-2, 0), (-1, 0), (1, 0), (2, 0)],
    2: [(-1, 0), (0, -1), (0, 1), (1, 0)],
    3: [(-1, -1), (-1, 1), (1, -1), (1, 1)]
}

# k = 폭탄의 개수
row_hap = [sum(lst) for lst in grid]
k = sum(row_hap)

# 중복 순열을 구해서 모든 경우의 수를 돌면서 계산함
bomb_case = []
for i in product([1, 2, 3], repeat=k):
    bomb_case.append(i)

max_bomb = 0
for bomb in bomb_case:
    arr = [row[:] for row in grid]

    bomb = list(bomb)
    idx = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                bomb_case = bomb[idx]
                bomb_range = bomb_dct[bomb_case]

                for di, dj in bomb_range:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        if arr[ni][nj] == 0:
                            arr[ni][nj] = 1

                idx += 1

    after_row_hap = [sum(lst) for lst in arr]
    hap = sum(after_row_hap)
    max_bomb = max(max_bomb, hap)

print(max_bomb)