# 백준_5430_AC (G5)
"""
## [문제 정리]
- AC언어 : 정수 배열에 연산을 하기 위해 만든 언어
    - 두 가지 함수 R(뒤집기), D(버리기) 존재
- 함수 R, D
    - R(뒤집기)
        - 배열에 있는 수의 순서를 뒤집는 함수
    - D(버리기)
        - 배열에 있는 첫 번째 수를 버리는 함수
        - 배열이 비어있는데 D를 사용할 경우 에러 발생
    - 조합해서 한 번만 사용 가능
        - 예시 :
            - "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수
            - "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수
- 배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하시오.
"""
from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = input()

    # arr 입력 파싱
    if n == 0:
        dq = deque()

    else:
        arr = arr[1 : -1]       # 대괄호 제거
        if arr:
            dq = deque(map(int, arr.split(',')))
        else:
            dq = deque()

    # R의 실행여부를 관리할 변수 선언
    is_reversed = False
    # 에러 여부를 관리할 변수 선언
    error = False

    # arr 순회 후 함수 실행
    for alpha in p:
        if alpha == 'R':
            is_reversed = not is_reversed
        elif alpha == 'D':
            if not dq:
                error = True
                break

            if is_reversed:
                dq.pop()
            else:
                dq.popleft()

    if error:
        print('error')
    else:
        if is_reversed:
            dq.reverse()
        print('[' + ','.join(map(str, dq)) + ']')