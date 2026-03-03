# 백준_1141_접두사 (S1)
"""
## [문제 정리]

- 접두사 X 집합 :
    - 집합의 어떤 한 단어가, 다른 단어의 접두어가 되지 않는 집합
    - 예를 들어 : 
        - {hello}, {hello,goodbye,giant,hi}, {}
          -> 접두사 X 집합
        - {hello, hell}, {giant, gig, g}
          -> 접두사 X 집합 X

- 단어 N개로 이루어진 집합이 주어졌을 때,
  접두사 X 집합인 부분집합의 최대 크기 출력
"""
N = int(input())

words = set()
for _ in range(N):
    word = input().strip()
    words.add(word)

sorted_words = sorted(list(words), key=lambda x: len(x))
M = len(sorted_words)

remove = set()
for idx1 in range(M):
    for idx2 in range(idx1 + 1, M):
        word, length = sorted_words[idx1], len(sorted_words[idx1])

        if sorted_words[idx2][0:length] == word:
            remove.add(word)

result = [w for w in sorted_words if w not in remove]

print(len(result))