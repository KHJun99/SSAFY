import sys

sys.stdin = open('s_input.txt')

def my_count(lst, str):
    count = 0
    for i in range(len(lst)):
        if lst[i] == str:
            count += 1
    return count


T = int(input())
for i in range(1, T + 1):
    N = int(input())
    line1 = [[] for _ in range(5001)]
    for j in range(N):
        A, B = list(map(int, input().split()))
        for line in range(A, B + 1):
            line1[line].append(1)

    P = int(input())
    result = []
    for k in range(P):
        c = int(input())
        result.append(my_count(line1[c], 1))

    print(f'#{i} {" ".join(map(str, result))}')




