# 1486_장훈이의 높은 선반 (D4)
"""
문제
- N명의 직원이 높이가 B 이상의 물건을 사용하려고 한다.
- 각 점원의 키는 Hi로 나타내며, 탑을 쌓아서 선반 위의 물건을 사용하려 한다.
- 쌓는 탑은 점원 1명 이상으로 구성
- 탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 동일
- 높이가 B이상인 탑 중에서 높이가 가장 낮은 탑을 구하여라.

입력
- 첫 번째 줄 : T (테스트 케이스 개수)
- 두 번째 줄 : N (점원의 수), B (선반의 높이)
- 세 번째 줄 : S (점원들의 키 집합(공백으로 구분))

접근 방법
- 부분 집합을 구하여 합을 구한다.
- 합과 B의 차가 가장 작을 경우를 출력
"""
import sys
sys.stdin = open('input.txt', 'r')


def all_subset(lst):
    n = len(lst)
    res = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (i << i):
                subset.append(lst[i])
        res.append(subset)
    return res


def min_diff():
    pass

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    subsets = all_subset(height)
    hap = []
    for i in subsets:
        hap.append(sum(i))

    print(hap)
    exit()