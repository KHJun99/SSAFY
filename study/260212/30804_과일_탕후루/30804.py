# 백준_30804_과일_탕후루 (S2)
"""
Docstring for 260212.30804_과일_탕후루.30804

## [문제 정리]

- 긴 막대에 N개의 과일이 꽂혀있는 과일 탕후르를 만들었다.
- 과일의 각 종류에는 1부터 9까지의 번호가 존재
    - 앞쪽부터 차례로 S1, S2, ..., SN 번
- 과일 탕후루 요청사항 : 두 종류 이하로 사용
- 시간이 없어서 막대의 앞쪽과 뒤쪽에서 몇 개의 과일을 빼서 두 종류만 남기기로 결정
- 앞에서 a개, 뒤에서 b개의 과일을 빼면 S(a+1), S(a+2), ..., S(N-b-1), S(N-b)번 과일
    - 총 N - (a + b)개로 이루어진 탕후루 완성
- 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루에서
    - 과일의 개수가 가장 많은 탕후루의 과일 개수를 구하시오.
"""
# def make_Tanghulu(n, lst):
#     max_lenght = float("-inf")

#     for start in range(n):
#         fruits_count = {}
#         for end in range(start, n):
#             fruit = lst[end]
#             # get() 메서드는 키가 없을 때 반환할 기본값 설정 가능 -> keyerror 방지
#             # get(키, 키가 없을 때 반환할 값)
#             fruits_count[fruit] = fruits_count.get(fruit, 0) + 1

#             if len(fruits_count) <= 2:
#                 max_lenght = max(max_lenght, end - start + 1)
#             else:
#                 break

#     print(max_lenght)
def make_Tanghulu(n, lst):
    left, right = 0, 0
    max_length = float('-inf')

    fruits_count = {}

    while left != n and right < n:
        fruit = lst[right]
        fruits_count[fruit] = fruits_count.get(fruit, 0) + 1

        if len(fruits_count) <= 2:
            max_length = max(max_length, right - left + 1)
            right += 1
        
        else:
            fruits_count[lst[left]] -= 1
            if fruits_count[lst[left]] == 0:
                del fruits_count[lst[left]]
            left += 1
            right += 1
    
    print(max_length)



N = int(input())

fruits = list(map(int, input().split()))

make_Tanghulu(N, fruits)