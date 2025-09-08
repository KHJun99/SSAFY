# 부분 수열의 합 (D3)
"""
문제
- A1, A2, ... , AN의 N개의 자연수가 주어진다.
- 최소 1개 이상의 수를 선택하여 합이 K가 되는 경우의 수를 구하여라.

입력
- 첫 번째 줄 : 테스크 케이스 T
- 두 번째 줄 : 자연수 N, K
- 세 번째 줄 : N개의 자연수 수열
"""
import sys
sys.stdin = open('sample_input.txt', 'r')


def subsequence(arr):
    n = len(arr)                        # 원소의 개수
    result_list = []                    # 생성된 부분 수열 저장
    for i in range(1 << n):             # 부분 수열 개수
        subset = []                     # 부분수열 담기 위함
        for j in range(n):              # 원소의 수만큼 비트를 비교함
            if i & (1 << j):
                subset.append(arr[j])   # 부분 수열 만들기
        result_list.append(subset)
    return result_list


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    subsequence_lst = subsequence(arr)
    for i in range(len(subsequence_lst)):
        for j in range(len(subsequence_lst[i])):
