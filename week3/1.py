# 0커플

# [문제해설] - hash table, 절대값 개수
# 출력 : 점수 배열 > 소개팅에 실패한 2명의 점수 합
# hash table > 현재 내 점수와 같고 부호만 반대인 사람의 존재 파악
# 커플조건 = 점수 합이 0 > 전체 점수 = 2명 점수의 합
n = input()
scores = list(map(int, input().split()))

print(sum(scores))

# [정답 풀이]
import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input())
dic = defaultdict()
arr = list(map(int, input().split()))
for i in arr:
    if abs(i) in dic:
        dic.pop(abs(i))
    else:
        dic[i] = 1
print(sum(dic.keys()))