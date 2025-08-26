matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.
# def length_str(str):
#     count = 0
#     for _ in str:
#         count += 1
#     return count

matrix_len = 0
for i in matrix:
    matrix_len += 1
    
print(matrix_len)

temporary_len = 0
for numbers in range(matrix_len):
    for _ in matrix[numbers]:
        temporary_len += 1
    if temporary_len <= 4:
        print(f'{matrix[numbers]}리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.')        
    temporary_len = 0

for i in range(matrix_len):
    for j in range(len(matrix[i])):
        a = matrix[i][j]
        print(f'matrix의 {i}, {j} 번째 요소의 값은 {a}')