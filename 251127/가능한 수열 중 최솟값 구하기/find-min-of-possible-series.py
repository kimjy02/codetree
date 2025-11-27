n = int(input())

# Please write your code here.
result = ""

def is_valid(seq):
    length = len(seq)
    # 마지막 부분부터 비교
    for k in range(1, length // 2 + 1):
        # 끝에서 k자리와 그 앞 k자리가 같으면 실패
        if seq[-k:] == seq[-2*k:-k]:
            return False
    return True

def dfs(seq):
    global result
    # 이미 답을 찾았으면 종료
    if result:
        return
    
    # 길이 완성되면 저장
    if len(seq) == n:
        result = seq
        return
    
    # 사전순 → 4 → 5 → 6 순서
    for num in "456":
        new_seq = seq + num
        if is_valid(new_seq):
            dfs(new_seq)

dfs("")
print(result)
