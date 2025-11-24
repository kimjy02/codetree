n, m, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max_arr = [[0] * (n - (m - 1)) for _ in range(n)]

# 리스트를 전달하면, 거기서 C 이하로 제곱합이 최대인 값을 반환해주는 dfs 함수 정의
def max_squared(lst, idx, weight_hap, squared_hap):
    if weight_hap > c:
        return 0

    if idx == m:
        return squared_hap

    case1 = max_squared(lst, idx + 1, weight_hap, squared_hap)
    case2 = max_squared(lst, idx + 1, weight_hap + lst[idx], squared_hap + (lst[idx] * lst[idx]))

    return max(case1, case2)

for i in range(n):
    for j in range(n - (m - 1)):
        check_lst = arr[i][j:j+m]
        max_arr[i][j] = max_squared(check_lst, 0, 0, 0)

answer = 0

for i1 in range(n):
    for j1 in range(n - m + 1):
        for i2 in range(n):
            for j2 in range(n - m + 1):

                # 같은 행이라면 겹치면 안 됨
                if i1 == i2 and not (j1 + m <= j2 or j2 + m <= j1):
                    continue

                answer = max(answer, max_arr[i1][j1] + max_arr[i2][j2])

print(answer)