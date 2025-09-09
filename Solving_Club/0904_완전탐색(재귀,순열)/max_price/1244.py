# [S/W 문제해결 응용] 2일차 - 최대 상금 (D3)
"""
문제
- 주어진 숫자판들 중에 두 개를 선택해서 정해진 횟수만큼 자리를 교환할 수 있다.
- 정해진 횟수만큼 교환이 끝나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산
- 숫자판의 오른쪽 끝에서 부터 1원, 왼쪽으로 한자리씩 갈수록 10의 배수만큰 커진다
- ex) 8, 8, 8, 3, 2 -> 88832원의 보너스 상금
- 최대 보너스 상금을 구하시오.

조건
- 최대 자릿수는 6자리
- 최대 교환 횟수 = 10번
"""
import sys
sys.stdin = open('input.txt', 'r')


def swap(a, b):
    plate[a], plate[b] = plate[b], plate[a]

def max_idx(lst):
    max_val = float('-inf')
    idx = 0
    for i in range(len(lst)):
        if max_val < lst[i]:
            max_val = lst[i]
            idx = i

    return idx

def dfs(count):
    price = ''.join(plate)
    if max_price > price:
        return

    if count == cnt:
        return
    idx = max_idx(plate)
    swap(idx, 0)
    dfs(count + 1)




T = int(input())
for tc in range(1, T + 1):
    plate, cnt = map(int, input().split())

    max_price = float('-inf')

    dfs(0)


    # print(f'#{tc} {}')