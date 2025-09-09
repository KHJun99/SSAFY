# [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드 (D3)
"""
암호 규칙
1. 8개의 숫자 구성되어 있다.
2. 숫자 하나 당 7개의 비트로 암호화 되어 있다.
   즉, 암호코드의 가로 길이는 56
3. 암호코드의 길이가 56이 아닌 코드는 주어지지 않는다.
4. 올바른 암호 코드 = (홀수 자리 합 * 3) + (짝수 자리 합) -> 10의 배수
"""
# def binary_password(lst, n, m):
#     password = []
#     for i in range(n):
#         for j in range(m - 6):
#             if len(password) == 8:
#                 break
#             if ''.join(lst[i][j:j+7]) == '0001101':
#                 num = 0
#                 password.append(num)
#                 j += 7
#             elif ''.join(lst[i][j:j+7]) == '0011001':
#                 num = 1
#                 password.append(num)
#                 j += 7
#             elif ''.join(lst[i][j:j+7]) == '0010011':
#                 num = 2
#                 password.append(num)
#                 j += 7
#             elif ''.join(lst[i][j:j+7]) == '0111101':
#                 num = 3
#                 password.append(num)
#                 j += 7
#             elif ''.join(lst[i][j:j+7]) == '0100011':
#                 num = 4
#                 password.append(num)
#                 j += 7
#             elif ''.join(lst[i][j:j+7]) == '0110001':
#                 num = 5
#                 password.append(num)
#                 j += 7
#             elif ''.join(lst[i][j:j+7]) == '0101111':
#                 num = 6
#                 password.append(num)
#                 j += 7
#             elif ''.join(lst[i][j:j+7]) == '0111011':
#                 num = 7
#                 password.append(num)
#                 j += 7
#             elif ''.join(lst[i][j:j+7]) == '0110111':
#                 num = 8
#                 password.append(num)
#                 j += 7
#             elif ''.join(lst[i][j:j+7]) == '0001011':
#                 num = 9
#                 password.append(num)
#                 j += 7
#             else:
#                 continue
#
#     return password
import sys
sys.stdin = open('input.txt', 'r')


def binary_password(lst,n,m):
    password = []
    for i in range(n):
        j = m
        while j >= 0:
            windows = ''.join(lst[i][j:j - 7:-1])
            if len(password) == 8:
                return password
            if windows in pw:
                password.append(pw[windows])
                j -= 7
            else:
                j -= 1
    return password


pw = {
    '1011000' : 0,
    '1001100' : 1,
    '1100100' : 2,
    '1011110' : 3,
    '1100010' : 4,
    '1000110' : 5,
    '1111010' : 6,
    '1101110' : 7,
    '1110110' : 8,
    '1101000' : 9
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())        # N : 배열의 세로 크기, M : 배열의 가로 크기
    arr = [list(input()) for _ in range(N)]

    password = binary_password(arr, N, M)
    password.reverse()
    pw_sum = 0

    if ((sum(password[0:8:2]) * 3) + sum(password[1:8:2])) % 10 == 0:
        for i in password:
            pw_sum += i
    else:
        pw_sum = 0

    print(f'#{tc} {pw_sum}')
