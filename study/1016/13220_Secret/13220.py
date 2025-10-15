# 백준_13220_Secret (G5)
"""
## [문제 정리]
- 비밀번호는 N개의 공백으로 구분된 정수로 이루어져 있다.
- 앨리스는 자신이 고안한 암호화 방식, 즉 루프 안에 코드를 작성하는 방식 사용
- 예 )
    - 비밀번호 : "37 20 71 33 97"
    - 앨리스 비밀번호 : "20 71 33 97 37"
    - 시작점 : 5번째 정수 (단, 시작점은 앨리스 마음대로 정할 수 있음)
- 이브는 앨리스의 암호화된 메시지 2개를 가지고 있음
- 앨리스가 같은 비밀번호를 두 번 보냈을 가능성을 구하시오.
"""
N = int(input())
pw1 = list(map(int, input().split()))
pw2 = list(map(int, input().split()))

pattern = ''.join(map(str, pw1 + pw1))
pw = ''.join(map(str, pw2))

if pw in pattern:
    print('YES')
else:
    print('NO')