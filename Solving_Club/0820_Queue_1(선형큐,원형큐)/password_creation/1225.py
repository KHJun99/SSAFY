# [S/W 문제해결 기본] 7일차 - 암호 생성기

"""
문제
- 8개의 숫자를 입력 받는다.
- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
- 다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.
이와 같은 작업을 한 사이클이라 한다.
- 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다.
"""
import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    password = list(map(int, input().split()))

    while password[-1] != 0:
        for i in range(1, 6):
            tmp = password[0]
            if tmp - i > 0:
                password.append(tmp - i)
                password.pop(0)
            else:
                password.append(0)
                password.pop(0)
                break

    print(f'#{tc}', *password)