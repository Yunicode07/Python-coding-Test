import sys
import os

# 예제.txt
sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"))

input = sys.stdin.readline

N = int(input())

# dp 리스트 생성
dp = [(0,0)] * 41
dp[0] = (1,0)
dp[1] = (0,1)

# 40보다 작거나 같은 자연수 또는 0
for i in range(2,41):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

# _는 변수 안 쓸 때
for _ in range(N):
    n = int(input())
    print(dp[n][0], dp[n][1])