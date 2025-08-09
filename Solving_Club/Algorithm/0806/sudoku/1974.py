import sys

sys.stdin = open('input.txt')

T = int(input())
puzzle = []
for i in range(9):
    arr = list(map(int, input().split()))
    puzzle.append(arr)

