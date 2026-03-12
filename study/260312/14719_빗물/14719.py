# 백준_14719_빗물 (G5)
"""
## [문제 정리]

- 2차원 세계에 블록이 쌓여있다.
- 비가 오면 블록 사이에 빗물이 고인다.
- 비는 충분히 많이 올 때, 고이는 빗물의 총량을 구하시오.
"""
H, W = map(int, input().split())
heights = list(map(int, input().split()))

left, right = [], []

for idx in range(W):
    left_lst = heights[:idx]
    right_lst = heights[idx:]

    left.append(max(left_lst) if left_lst else 0)
    right.append(max(right_lst) if right_lst else 0)

result = 0
for idx in range(W):
    amount = min(left[idx], right[idx]) - heights[idx]
    
    if amount >= 0:
        result += amount

print(result)

# H, W = map(int, input().split())
# heights = list(map(int, input().split()))

# # 최고 높이의 인덱스 찾기
# max_height, max_idx = 0, 0
# for idx, height in enumerate(heights):
#     if height > max_height:
#         max_height = height
#         max_idx = idx

# # 왼쪽 구간의 최대 높이 
# left_max = float('-inf')
# for left in range(max_idx):
#     if heights[left] > left_max:  
#         left_max = heights[left]  

# # 오른쪽 구간의 최대 높이
# right_max = float('-inf')
# for right in range(W - 1, max_idx, -1):  
#     if heights[right] > right_max:        
#         right_max = heights[right]         

# # 빗물 계산
# amount = 0
# for idx, height in enumerate(heights):
#     if idx < max_idx:
#         # 왼쪽 구간: 왼쪽 최대와 현재 높이 차이
#         if height < left_max:
#             amount += left_max - height
#     elif idx > max_idx:
#         # 오른쪽 구간: 오른쪽 최대와 현재 높이 차이
#         if height < right_max:
#             amount += right_max - height

# print(amount)

