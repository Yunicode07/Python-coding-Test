import sys
import os

# 예제.txt
sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"))

input = sys.stdin.readline

N = int(input())
# 줄바꿈 제거
S = input().strip()

# S.count('O') > S.count('X') 이 공식은 무조건 O가 더 많을때
# "과반수 이상" 라는 조건을 충족하기 위해 (N + 1) // 2
if S.count('O') >= (N + 1) // 2:
    print('Yes')
else:
    print('No')

# 추천 리뷰
# print('Yes' if S.count('O') >= (N+1) // 2 else 'No')