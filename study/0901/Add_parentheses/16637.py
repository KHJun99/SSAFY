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
def apply(a, op, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b


def cacu(lst):
    n = len(lst)
    stack = []
    temp = 0
    # 괄호 없이 계산
    for idx in range(n):
        stack.append(lst[idx])
        if len(stack) == 3:
            c = stack.pop()
            b = stack.pop()
            a = stack.pop()
            stack.append(apply(a, b, c))
    if len(stack) == 1:
        temp = stack.pop()
        stack.clear()

    return temp


N = int(input())
exp = list(input())

# 숫자는 int 형으로 변환
for i in range(len(exp)):
    if exp[i].isdigit():
        exp[i] = int(exp[i])

result= []
result.append(cacu(exp))
for i in range(1, N, 2):
    temp1 = exp[:]
    temp2 = exp[:]
    temp1[i-1:i+2] = [apply(temp1[i-1], temp1[i], temp1[i+1])]
    result.append(cacu(temp1))
    if i + 1 < len(temp2):  # 최소 (a op b) 성립 체크
        positions = []  # 괄호 칠 연산자 인덱스들 모으기
        p = i
        while p + 1 < len(temp2):  # p-1, p, p+1 접근 가능
            positions.append(p)
            p += 4  # 서로 안 겹치도록 4칸 간격

        # 원본 temp2 기준으로 먼저 값 계산 (각 구간은 서로 불연속)
        vals = {p: apply(temp2[p - 1], temp2[p], temp2[p + 1]) for p in positions}

        # 인덱스 붕괴 방지를 위해 '오른쪽부터' 치환
        for p in reversed(positions):
            temp2[p - 1:p + 2] = [vals[p]]

        result.append(cacu(temp2))
    # j = i + 4
    # if j + 1 < len(temp2):  # FIX: 경계 체크 보강
    #     # 두 괄호의 값은 '원본 temp2' 기준으로 먼저 계산
    #     v_left = apply(temp2[i - 1], temp2[i], temp2[i + 1])  # FIX: -2 보정 제거
    #     v_right = apply(temp2[j - 1], temp2[j], temp2[j + 1])  # FIX: -2 보정 제거
    #     # 오른쪽 덩어리부터 치환 → 왼쪽 인덱스가 안 흔들림
    #     temp2[j - 1:j + 2] = [v_right]  # FIX: 동시대입 제거, 우측 먼저
    #     temp2[i - 1:i + 2] = [v_left]  # FIX: 좌측 나중에 대입
    #     result.append(cacu(temp2))

print(max(result))