# [파이선 S/W 문제해결 기본] 4일차 - 반복문자 지우기
import sys
sys.stdin = open('4873_input.txt')


T = int(input())
for tc in range(1, T + 1):
    arr = str(input().strip())
    stack = []
    for i in range(len(arr)):
        if stack and stack[-1] == arr[i]:
            stack.pop()
        else:
            stack.append(arr[i])
    print(f'#{tc} {len(stack)}')
