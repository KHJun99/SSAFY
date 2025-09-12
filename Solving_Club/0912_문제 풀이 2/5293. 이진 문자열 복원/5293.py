T = int(input())

for tc in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    # 00 01 10 11

    """
    조합 중 아무거나 해도 가능

    1. 목적
    원래 문자열로 가능한지

    2. 조건
    A+B+C+D>=1 보장
    조건 만족하는 문자열 없다면 impossible

    3. 구현
    큐에 넣고 만족하는 경우로 다 하고, 안되면 impossible
    -> 완탐 돌려서 압축 하고 압축 하나라도 되면 바로 종료하고 출력, 안되면 impossible
    압축을 하면 01 1개 예외처리
    가능한 아무 문자열이나 가능하다 -> 자동 가지치기'
    dfs 하니까 시간초과

    역으로 돌려서
    1. 비트연산자로 0과 1로 된 순열 
    2. 해당 순열이 주어진 값과 같은지 
        같으면 flag 출력하고 전체 종료

    탐색 자제는 아예 불가능

    구현으로

    오일러 경로
    """
    answer = ""
    one_in = 0
    one_out = 0
    zero_in = 0
    zero_out = 0

    zero_in += a
    zero_out += a
    one_in += b
    zero_out += b
    zero_in += c
    one_out += c
    one_in += d
    one_out += d

    if zero_out == zero_in and one_out == one_in:
        if b == 0:
            if a > 0 and d > 0:
                answer = "impossible"
            elif a > 0:
                answer = "0" * (a + 1)
            else:
                answer = "1" * (d + 1)
        else:
            answer = "0" * (a + 1) + ("10" * (b - 1)) + "1" * (d + 1) + "0"
    elif zero_out == zero_in + 1 and one_in == one_out + 1:
        answer = "0" * (a + 1) + "10" * c + "1" * (d + 1)
    elif one_out == one_in + 1 and zero_in == zero_out + 1:
        answer = "1" * (d + 1) + "01" * b + "0" * (a + 1)
    else:
        answer = "impossible"

    print(f"#{tc} {answer}")