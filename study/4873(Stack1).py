# [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기
def remove_str(word):
    stack = []
    for ch in word:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return len(stack)

t = int(input())

for i in range(1, t + 1):
    word = input().strip()
    
    result = remove_str(word)
    print(f'#{i} {result}')
    
        