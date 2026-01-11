# 백준_2529_부등호 (S1)
"""
## [문제 정리]
- 두 종료의 부동호 기호 '<'와 '>'가 k개 나열된 순서열 A가 존재
- 부등호 기호 앞뒤에 서로 다른 한 자릿수 숫자를 넣어서 모든 부등호 관계를 만족
- 예시
    - A => < < < > < < > < >
    - 3 < 4 < 5 < 6 > 1 < 2 < 8 > 7 < 9 > 0
    - 3456128790 -> 부등호 관계를 만족하는 정수
    - 5 < 6 < 8 < 9 > 0 < 2 < 3 > 1 < 7 > 4
    - 5689023174 -> 부등호 관계를 만족하는 정수
- k개의 부등호 순서를 만족하는 (k + 1)자리의 정수 중
- 최댓값과 최솟값을 구하시오. (단, 선택된 숫자는 모두 달라야 한다.)
"""
def check(a, b, sign):
    if sign == '<':
        return a < b
    else:
        return a > b


def make_num(depth, num_str):
    if depth == k + 1:
        results.append(num_str)
        return

    for num in range(10):
        if visited[num]:
            continue

        if depth > 0:
            prev_num = int(num_str[-1])
            curr_sign = signs[depth - 1]

            if not check(prev_num, num, curr_sign):
                continue

        visited[num] = True
        make_num(depth + 1, num_str + str(num))
        visited[num] = False

k = int(input())
signs = input().split()
visited = [False] * 10
results = []

make_num(0, "")

# results.sort()

print(results[-1])
print(results[0])