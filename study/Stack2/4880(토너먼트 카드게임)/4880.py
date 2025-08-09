import sys

sys.stdin = open('sample_input (2).txt')

def win(p1, p2):
    a, a_val = p1
    b, b_val = p2
    # 가위(1) 바위(2) 보(3)
    if a_val == b_val:  # 비길 경우
        return p1
    if a_val == 1 and b_val == 3:  # 가위 vs 보
        return p1
    if a_val == 3 and b_val == 1:
        return p2
    if a_val == 1 and b_val == 2:  # 가위 vs 바위
        return p2
    if a_val == 2 and b_val == 1:
        return p1
    if a_val == 2 and b_val == 3:  # 바위 vs 보
        return p2
    if a_val == 3 and b_val == 2:
        return p1
        

def rsp(lst, n):
    if len(lst) == 1:
          return lst[0]

    # 두 개의 그룹으로 나누기
    mid = (n - 1) // 2
    l_group = lst[ : mid + 1]
    r_group = lst[mid + 1 : ]

    # 각 그룹의 승자를 재귀 호출로 구함
    left_winner = rsp(l_group, len(l_group))
    right_winner = rsp(r_group, len(r_group)) 

    # # 승자 선출 과정
    # for i in range(0, len(l_group), 2):
    #     if i + 1 < len(l_group):        # 그룹에 인원이 짝수인 경우
    #         final.append(win(l_group[i], l_group[i+1]))
    #     else:                           # 그룹에 인원이 홀수인 경우 >> 다음 라운드 부전승
    #         final.append(l_group[i])

    # for i in range(0, len(r_group), 2):
    #     if i + 1 < len(r_group):        
    #         final.append(win(r_group[i], r_group[i+1]))
    #     else:                           
    #         final.append(r_group[i])

    return win(left_winner, right_winner)
          

T = int(input())
for tc in range(1, T + 1):
    N = int(input())        # 인원 수
    student = list(map(int, input().split()))
    
    # 등번호와 값을 저장하기 위해
    num_name = [(i, val) for i, val in enumerate(student, start = 1)]

    result = rsp(num_name, N)
    winnder_idx = result[0]
    print(f'#{tc} {winnder_idx}')