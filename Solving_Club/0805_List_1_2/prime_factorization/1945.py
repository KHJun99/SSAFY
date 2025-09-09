import sys

sys.stdin = open('input.txt')


def find_prime(num):
    num_lst = [2, 3, 5, 7, 11]
    prime = []

    for i in num_lst:
        count = 0
        while num % i == 0:
            count += 1
            num //= i
        prime.append(count)

    return prime


T = int(input())

for i in range(1, T + 1):
    num = int(input())

    # join 메소드는 문자열 리스트에서만 작동
    print(f'#{i} {" ".join(map(str, find_prime(num)))}')