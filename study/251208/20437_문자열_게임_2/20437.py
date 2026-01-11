# 백준_20437_문자열_게임_2 (G5)
"""
## [문제 정리]
- 게임 진행 방식
    1. 알파벳 소문자로 주어진 문자열 W 제공
    2. 양의 정수 K 제공
    3. 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
    4. 어던 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가
       해당 문자로 같은 가장 긴 문자열의 길이를 구한다.

- T번 반복했을 때의 결과 출력
"""
# 시간초과

# import sys
# input = sys.stdin.readline
#
# def start_end_same_word(words, cnt):
#     # 4번 조건: 어떤 문자를 K개 포함하면서 그 문자로 시작하고 끝나는 가장 긴 부분 문자열
#     max_length = 0
#     n = len(words)
#     word_set = set(words)
#
#     for word in word_set:
#         for i in range(n):
#             for j in range(i + 1, n + 1):
#                 tmp_word = words[i:j]
#                 # 특정 문자를 cnt개 포함하고, 그 문자로 시작하고 끝나는지 확인
#                 if tmp_word.count(word) == cnt and tmp_word[0] == word and tmp_word[-1] == word:
#                     if max_length < len(tmp_word):
#                         max_length = len(tmp_word)
#
#     return max_length
#
#
# def min_length_word(words, cnt):
#     # 3번 조건: 어떤 문자를 K개 포함하는 가장 짧은 부분 문자열
#     tmp = []
#     n = len(words)
#     words_set = set(words)
#
#     # 각 문자에 대해 cnt개 포함하는 모든 부분 문자열 찾기
#     for word in words_set:
#         for i in range(n):
#             for j in range(i + 1, n + 1):
#                 tmp_word = words[i:j]
#                 if tmp_word.count(word) == cnt:
#                     tmp.append(tmp_word)
#
#     # 조건을 만족하는 부분 문자열이 없으면 -1 반환
#     if not tmp:
#         return -1, -1
#
#     # 최소 길이 찾기
#     min_length = float('inf')
#     for w in tmp:
#         if min_length > len(w):
#             min_length = len(w)
#
#     # 최대 길이 찾기
#     longest_word = start_end_same_word(words, cnt)
#     return min_length, longest_word
#
#
# T = int(input())
# for _ in range(T):
#     W = input()
#     K = int(input())
#
#     # K가 1이면 항상 길이 1
#     if K == 1:
#         print("1 1")
#         continue
#
#     smallest, longest = min_length_word(W, K)
#
#     if smallest == -1:
#         print(-1)
#     else:
#         print(smallest, longest)

def solve(W, K):
    # 각 문자의 위치를 저장
    char_positions = {}
    for i, char in enumerate(W):
        if char not in char_positions:
            char_positions[char] = []
        char_positions[char].append(i)

    min_length = float('inf')
    max_length = 0
    found = False

    # 각 문자에 대해 K개씩 묶어서 확인
    for char in char_positions:
        positions = char_positions[char]
        # K개 미만이면 불가능
        if len(positions) < K:
            continue

        found = True
        # i번째부터 (i+K-1)번째까지가 K개를 포함하는 부분 문자열
        for i in range(len(positions) - K + 1):
            start = positions[i]
            end = positions[i + K - 1]
            length = end - start + 1

            # 3번 조건: 최소 길이
            min_length = min(min_length, length)
            # 4번 조건: 자동으로 같은 문자로 시작/끝
            max_length = max(max_length, length)

    if not found:
        return -1, -1

    return min_length, max_length


T = int(input())
for _ in range(T):
    W = input()
    K = int(input())

    if K == 1:
        print("1 1")
        continue

    min_len, max_len = solve(W, K)

    if min_len == -1:
        print(-1)
    else:
        print(min_len, max_len)