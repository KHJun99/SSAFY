# 나무의 키
"""
조건
1. 하루에 한 나무에 물을 줄 수 있다.
2. 홀수 번째 날은 키가 1 자라고, 짝수 번재 날은 키가 2 자란다.
3. 물을 주지 않는 경우도 가능

문제

N개의 나무가 있다. 초기의 각 나무의 키가 주어진다.
하루에 한 나무에 물을 줄 수 있다.
첫 날은 물을 준 나무의 키가 1 자라고, 둘째 날은 물을 준 나무의 키가 2 자라고,
셋째 날은 물을 준 나무의 키가 1 자라는 식으로, 홀수 번째 날은 키가 1 자라고 짝수 번째 날은 키가 2 자란다.
모든 나무의 키가 처음에 가장 키가 컸던 나무와 같아지도록 할 수 있는 최소 날짜 수를 계산하라.
어떤 날에는 물을 주는 것을 하지 않을 수도 있다.
예를 들어 나무가 2그루이고 각각의 높이가 4와 2라고 하자.
첫째 날에 물을 주게 되면, 나무의 높이를 모두 4로 만들기 위해서는 3일째까지 물을 주어야 한다.
둘째 날은 아무 일도 안 하게 된다. 하지만, 첫째 날을 쉬고 둘째 날에 물을 주면 2일 만에 나무의 높이가 모두 4가 된다.
"""
import sys
sys.stdin = open('tree_sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = list(map(int, input().split()))

    day = 0
    diff_lst = []
    tall_tree = max(tree)
    if sum(tree) // N == max(tree):
        day = 0

    else:
        for i in range(N):
            if tree[i] != tall_tree:
                diff_lst.append(tall_tree - tree[i])

        q = sum(diff_lst) // 3 * 2
        day += q
        r = sum(diff_lst) % 3
        if r != 0:
            if r % 2 == 0:
                day += 2
            else:
                day += 1

    print(f'#{tc} {day}')

    # if N == 2:
    #     diff = max(tree) - min(tree)
    #     if diff % 2 == 0:
    #         day = 2 * (diff // 2)
    #     else:
    #         day = 1 * (diff % 2)
    # else:
    #     tall_tree = max(tree)
    #     diff_lst = []
    #     for i in range(N):
    #         if tree[i] != tall_tree:
    #             diff_lst.append(tall_tree - tree[i])
    #
    #     for i in range(len(diff_lst)):
    #         if diff_lst[i] % 2 == 0:
    #             day += 2 * (diff_lst[i] // 2)
    #         else:
    #             day += 1 * (diff_lst[i] % 2)
