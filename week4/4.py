# 주차 구역 나누기
# 복습강의를 통해 다시 공부했는데도 아직 공식 이해를 잘 못하겠음 DP문제를 더 풀어보자


import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
dp = deque()

dp.append(0)
dp.append(0)
dp.append(1)
for i in range(3, n+1):
    dp.append((2 * ( i - 1)+1) * dp[-1] + dp[-2])
    dp.popleft()
print(dp[-1] % 100000007)