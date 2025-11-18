import heapq

move_dct = {"U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)}

change_dct = {"U": "D",
             "D": "U",
             "L": "R",
             "R": "L"}

n, m, t, k = map(int, input().split())
r, c, d, v = [], [], [], []
for _ in range(m):
    ri, ci, di, vi = input().split()
    r.append(int(ri)-1)
    c.append(int(ci)-1)
    d.append(di)
    v.append(int(vi))

# Please write your code here.
marbles_dct = {idx: (r[idx-1], c[idx-1], d[idx-1], v[idx-1]) for idx in range(1, m+1)}
marbles_set = set([x for x in range(1, m+1)])
time = 0

while time < t:
    time += 1
    if not marbles_set: break

    visited_arr = [[[] for _ in range(n)] for _ in range(n)]
    iter_marbles = list(marbles_set)

    for marble_idx in iter_marbles:
        ni, nj, udlr, vel = marbles_dct[marble_idx]
        for _ in range(vel):
            di, dj = move_dct[udlr]
            ni += di
            nj += dj

            if ni < 0 or n <= ni or nj < 0 or n <= nj:
                ni -= di
                nj -= dj
                udlr = change_dct[udlr]
                di, dj = move_dct[udlr]
                ni += di
                nj += dj

        # marbles_dct 업데이트
        marbles_dct[marble_idx] = (ni, nj, udlr, vel)

        # arr가 0 이면 바로 입력,
        # 값이 있으면 해당 숫자, 지금 내 숫자 set에서 제거
            # 제거 후에는 그 값을 -1로 바꾸기
        # 값이 -1 이면, 지금 내 숫자 set에서 제거
        if len(visited_arr[ni][nj]) < k:
            heapq.heappush(visited_arr[ni][nj], (vel, marble_idx))
        else:
            heapq.heappush(visited_arr[ni][nj], (vel, marble_idx))
            velocity, pop_idx = heapq.heappop(visited_arr[ni][nj])
            marbles_set.remove(pop_idx)

print(len(marbles_set))