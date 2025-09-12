# 가능한 시험 점수 (D4)
"""
## [문제요약]

- 영준이는 N개의 시험 문제를 만들었음.
- 각 문제는 맞으면 배점만큼, 틀리면 0점을 받는다.
- 따라서 학생이 받을 수 있는 점수는 선택한 문제들의 배점 합으로 결정됨.
- 목표: 가능한 모든 점수의 경우의 수(서로 다른 점수의 개수)를 구하는 것.

## 예시
1. **Testcase 1**

   * 문제 개수: 3
   * 배점: 2, 3, 5
   * 가능한 점수 조합:

     * 0 (모두 틀림)
     * 2, 3, 5
     * 2+3=5, 2+5=7, 3+5=8, 2+3+5=10
   * 중복 제거 후 → {0, 2, 3, 5, 7, 8, 10}
   * 경우의 수: **7가지**

2. **Testcase 2**

   * 문제 개수: 10
   * 배점: 모두 1점
   * 가능한 점수 조합: 0 \~ 10까지 모든 정수
   * 경우의 수: **11가지**
"""
import sys
sys.stdin = open('sample_input.txt', 'r')


def number_of_case():
    if len(set(score)) == 1:
        return N + 1

    dp[0] = 1
    dp[1] = len(score)

    return False



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    score = list(map(int, input().split()))
    dp = [0] * (N + 1)

    a = number_of_case()
    print(a)

# 부분집합 사용한 코드 (런타임 에러 발생)
# # 종료 조건 : 모든 경우의 수를 다 체크 했을 때
# # 가지 개수 : 2개
# def recur(idx):
#     if idx == N:
#         result.append(subset[:])
#         return
#
#     # 1. 넣은 경우
#     subset.append(score[idx])
#     recur(idx + 1)
#     subset.pop()
#     # 2. 넣지 않은 경우
#     recur(idx + 1)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     score = list(map(int, input().split()))
#
#     result = []
#     subset = []
#     recur(0)
#
#     final = set()
#     for i in range(len(result)):
#         final.add(sum(result[i]))
#
#     print(f'#{tc}', len(final))


