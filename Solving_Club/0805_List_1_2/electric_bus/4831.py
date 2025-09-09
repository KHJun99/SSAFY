import sys

sys.stdin = open('sample_input.txt')

def charge_bus_count(K, N, L, M):
    charge_station = [False] * (N + 1)
    for i in range(L):
        charge_station[M[i]] = True

    count = 0
    position = 0

    while True:
        position += K

        # 종점에 도착하거나 넘으면 종료
        if position >= N:
            break

        # 충전소가 없다면 한 칸씩 뒤로 이동
        while position > 0 and not charge_station[position]:
            position -= 1

        # 뒤로 가다가 0까지 갔으면 도달 불가
        if position <= 0:
            return 0
        for i in range(1, L):
            if M[i] - M[i - 1] > K:
                return 0

        # 충전
        count += 1

    return count

# T : 노선 수
# K : 최대한 이동할 수 있는 정류장 수
# N : 종점 정류장 번호
# L : 충전기가 설치된 정류장 개수
# M : 충전기가 설치된 정류장 번호

T = int(input())
for i in range(1, T + 1):
    K, N, L = list(map(int, input().split()))
    M = list(map(int, input().split()))
    print(f'#{i} {charge_bus_count(K, N, L, M)}')