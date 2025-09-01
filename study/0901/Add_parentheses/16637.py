# 백준_16673_괄호 추가하기 (G3)
"""
1) 문제 개요 (Task)

- 0~9 사이 정수와 연산자 +, -, ×로 이뤄진 길이 N의 수식이 주어진다.
- 모든 연산자 우선순위 동일 → 기본 계산은 왼쪽에서 오른쪽 순서.
- 괄호 추가 허용: 단, 괄호 안에는 연산자 딱 1개(즉, 피연산자 2개)만 포함.
- 중첩/겹침 불가(괄호가 서로 겹치면 안 됨). 괄호 개수 제한 없음(0개도 가능).
- 목표: 괄호를 적절히 배치해 식의 결과 최댓값을 구하라.

예) 3+8×7-9×2

- 기본(좌→우): (3+8)=11, 11×7=77, 77-9=68, 68×2=136 → 136
- 괄호: 3+(8×7)-(9×2) = 3+56-18 = 41

2) 규칙/제약 (Subtasks & Rules)

- 수식 형태: 일반적으로 숫자-연산자-숫자-…-숫자 패턴.
- 괄호는 연속된 세 토큰(숫자-연산자-숫자)을 감싼다.
- 겹치기 금지: 인접한 두 연산자에 동시에 괄호를 씌울 수 없음.
- 결과는 음수가 될 수 있음(정수 범위 주의: 구현 시 64-bit 정수 권장).
"""
from collections import deque


def apply(a, op, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b


def caculator(lst):
    cacu = deque()
    while lst:
        element = lst.pop(0)
        # 숫자 처리 (한 자리수 전제)
        if element.isdigit():
            cacu.append(int(element))
        # 연산자 처리
        elif element in '+-*':
            # 직전에 숫자 한 개만 있을 때만 연산자 허용
            if len(cacu) == 1:
                cacu.append(element)
        else:
            # 그 외 토큰 무시
            continue
        # 요소를 넣은 "후"에 [숫자, 연산자, 숫자]가 되면 즉시 계산
        if len(cacu) == 3:
            a = cacu.popleft()
            b = cacu.popleft()
            c = cacu.popleft()
            cacu.append(apply(a, b, c))
    # 결과 반환: 정수 하나만 남아야 정상
    return cacu[0] if len(cacu) == 1 else None


N = int(input())
exp = list(input())

result = []

# 괄호를 넣지 않은 경우
result.append(caculator(exp))

for i in range(1, len(exp), 2):
    if exp[i] in '-+*':
        a = exp.pop(i - 1)
        b = exp.pop(i)
        c = exp.pop(i + 1)
        exp.insert(i, apply(a, b, c))
    result.append(caculator(exp))

print(result)
