from collections import deque
n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0]-1 for pos in marbles]
c = [pos[1]-1 for pos in marbles]

# Please write your code here.
time = 0
result = [x for x in range(m)]
marbles_dct = {x: (r[x], c[x]) for x in range(m)}

while True:
    if time >= t: break
    if not result: break
    time += 1

    for i in result:
        value_i, value_j = r[i], c[i]
        value = a[value_i][value_j]

        si, sj = marbles_dct[i]

        max_value = value
        temp_list = []
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = si + di, sj + dj
            if 0 <= ni < n and 0 <= nj < n:
                if a[ni][nj] > max_value:
                    max_value = a[ni][nj]
                    temp_list.append((ni, nj))
        if temp_list:
            max_i, max_j = temp_list[-1]
            marbles_dct[i] = (max_i, max_j)

    # 같은 위치의 값이 있는지 확인
    # 그러기 위해서 기존의 marbles_dct의 키, 밸류를 뒤집음

    grid_dct = {}
    for k, v in marbles_dct.items():
        if v in grid_dct:
            result.remove(k)
            result.remove(grid_dct[v])
        else:
            grid_dct[v] = k

print(len(result))