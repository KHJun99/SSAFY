# 문제 1 : 이상한 나라의 김싸피 ( 배점 40 점)

T = int(input())
for tc in range(1, T + 1):
    arr = list(input())
    arr.append('.')

    result = []
    res = []
    for i in range(len(arr)):
        if arr[i] != '.':
            result.append(arr[i])
        elif arr[i] == '.':
            result.insert(0, '.')
            res.append(result[::-1])
            result.clear()

    for i in range(len(res)):
        for j in range(len(res[i])):
            result.append(res[i][j])

    word = ''.join(result[:len(result) - 1])

    print(f'#{tc} {word}')