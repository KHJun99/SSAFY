arr = ['A', 'B', 'C', 'D', 'E']
path = []
N = 3


def recur(cnt, start):
    # N 명을 뽑으면 종료
    if cnt == N:
        print(*path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        # i번째를 골랐으니, 다음 선택은 i + 1 부터 고려
        # i번째에서 i + 1의 일부 조합도 만들기 때문
        recur(cnt + 1, i + 1)
        # recur(cnt + 1, i) -> i번째를 골랐으니, 다음 선택은 i 부터 고려 (중복을 허용하는 조합)
        path.pop()

recur(0, 0)