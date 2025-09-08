import sys

# 현재 파일과 같은 위치에 있는 input.txt 파일 열어서 input으로 가져가겠다.
sys.stdin = open('input.txt')

# input() 호출 시 'input.txt'의 한 줄 씩 읽어서 가져옴
# input 함수는 리턴값이 문자열

# 테스트 케이스 개수 설정 / 하드 코딩일 때는 숫자로 설정
T = int(input())
for tc in range(1, T + 1):
    N = int(input())        # 방의 가로 길이
    box_list = list(map(int, input().split()))

    drop = 0
    for i in range(N):
        count = 0
        for j in range(i + 1, N):
            if box_list[i] > box_list[j]:
                count += 1
        if drop < count:
            drop = count
    print(f'#{tc} {drop}')
