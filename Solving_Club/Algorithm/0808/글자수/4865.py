import sys

sys.stdin = open('4865_input.txt')

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    count = 0
    count_dict = dict()
    # str1의 알파벳이 str2에 몇 개씩 들어있는지 찾고, 찾은 값을 딕셔너리에 저장
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count += 1
            count_dict[str1[i]] = count
        count = 0
    max_val = 0
    # 생성된 딕셔너리의 value 값을 돌면서 최대값 구하기
    for value in count_dict.values():
        if value > max_val:
            max_val = value

    print(f'#{tc} {max_val}')