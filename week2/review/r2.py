# 2주차 2번 다시풀기

# [문제해설] - 문자열 처리(슬라이싱), 조건문
# 출력 : 문자열 > 집합의 개수
# 집합 한 개 > 같은 문자열들끼리 묶어 구성, i번 문자 !== i+1번 문자라면 다른 집합
# 문자열을 분리할 필요없이 문자열에서 분리되는 횟수만 알아도 집합 개수 계산 가능


# [정답 풀이]
import sys
input = sys.stdin.readline

n = int(input())
arr = input()
cnt = 0

for i in range(n - 1): # 문자열 분리 횟수 계산
    if arr[i + 1] == arr[i]:
        continue
    else:
        cnt += 1

print(cnt + 1)