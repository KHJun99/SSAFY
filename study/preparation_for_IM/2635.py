# 수 이어가기
"""
규칙
1. 첫 번째 수로 양의 정수
2. 두 번쨰 수는 양의 정수 중에서 하나 선택
3. 세 번째부터 이후에 나오는 모든 수는 앞의 앞의 수에서 앞의 수를 빼서 만든다.
4. 음의 정수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다.
"""
N = int(input())

max_len = 0
best = []
for i in range(1, N + 1):
    num1, num2 = N, i
    lst = [num1, num2]

    while True:
        nxt = num1 - num2
        if nxt < 0:
            break
        lst.append(nxt)
        num1, num2 = num2, nxt

    if len(lst) > max_len:
        max_len = len(lst)
        best = lst

print(len(best))
print(*best)