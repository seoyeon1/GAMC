# 2주차 1번 다시풀기

# [문제해설] - 구현
# 출력 : 합격자수/응시자수
# case 1 > 정수 원소들의 평균 계산, 평균이상인 원소들의 개수(합격자수) 계산


# [정답 풀이]
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T): # 케이스마다 적용해야 할 코드
    
    n = int(input()) # 응시자수
    arr = list(map(int, input().split())) # n명의 시험 성적
    avg = sum(arr) / n
    cnt = 0
    for s in arr:
        if s >= avg: # 합격자수 계산
            cnt += 1
    print("%d/%d" %(cnt, n))