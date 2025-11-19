n = int(input())

# Please write your code here.

if n <= 4:
    lst = [1, 2, 4, 8]
    print(lst[n-1])

else:
    lst = [0] * n
    lst[0], lst[1], lst[2], lst[3] = 1, 2, 4, 8
    for i in range(4, n):
        lst[i] = lst[i-1] + lst[i-2] + lst[i-3] + lst[i-4]
    print(lst[n-1])