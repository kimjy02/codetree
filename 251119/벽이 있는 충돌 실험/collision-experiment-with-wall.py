T = int(input())

move_dct = {"U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)}

change_dct = {"U": "D",
             "D": "U",
             "L": "R",
             "R": "L"}

for _ in range(T):
    N, M = map(int, input().split())
    x, y, d = [], [], []
    for _ in range(M):
        xi, yi, di = input().split()
        x.append(int(xi)-1)
        y.append(int(yi)-1)
        d.append(di)

    # Please write your code here.
    marbles_dct = {idx: (x[idx-1], y[idx-1], d[idx-1]) for idx in range(1, M+1)}
    marbles_set = set([x for x in range(1, M+1)])
    time = 0

    while time < 4 * N:
        time += 1
        if not marbles_set: break

        visited_arr = [[0] * N for _ in range(N)]
        iter_marbles = list(marbles_set)

        for marble_idx in iter_marbles:
            i, j, udlr = marbles_dct[marble_idx]
            di, dj = move_dct[udlr]
            ni, nj = i + di, j + dj

            if ni < 0 or N <= ni or nj < 0 or N <= nj:
                udlr = change_dct[udlr]
                ni, nj = i, j

            # marbles_dct 업데이트
            marbles_dct[marble_idx] = (ni, nj, udlr)

            # arr가 0 이면 바로 입력,
            # 값이 있으면 해당 숫자, 지금 내 숫자 set에서 제거
                # 제거 후에는 그 값을 -1로 바꾸기
            # 값이 -1 이면, 지금 내 숫자 set에서 제거
            if visited_arr[ni][nj] == 0:
                visited_arr[ni][nj] = marble_idx
            elif visited_arr[ni][nj] == -1:
                marbles_set.remove(marble_idx)
            else:
                marbles_set.remove(visited_arr[ni][nj])
                marbles_set.remove(marble_idx)
                visited_arr[ni][nj] = -1

    print(len(marbles_set))