# 1주차 4번 다시풀기

# [문제해설] - 1차원 배열
# 출력 : 배열에서 idx값이 소수인 숫자들의 합
# 요구사항 : idx가 소수인지 확인 > 배열에서 해당 위치의 값 추출 & 더하기

# [수학적 개념] - 소수, 에라소트테네스의 체
# 소수 : 정수 n이 주어질 때, 1, -1, n으로만 나눠 떨어지는 1 이외의 정수
# 에라토스테네스의 체 : 가장 효율적인 소수찾기 방법
# 2부터 n-1까지 n이 소수라면 이후 n의 배수는 모두 제외 > 해당 숫자에 도착하기 전에 이미 소수가 아님을 판단하는 기법

# [정답 풀이]
import sys
input = sys.stdin.readline

# 함수 : 소수 판단
def prime(n):
    ch = [True] * (n+1) # 소수판딘 배열
    m = int(n**.5) # 제곱근

    for i in range(2, m+1):
        if ch[i]: # i가 소수라면
            for j in range(i+i, n+1, i): # 소수판단에서 i의 배수 제외
                ch[j] = False
    
    return [i for i in range(2, n+1) if ch[i]] # 소수 배열 생성

N = int(input())
P = prime(N)

A = list(map(int, input().split()))
res = 0

for i in P: # 소수배열의 값을 idx로 하는 숫자들의 합
    res += A[i-1]

print(res)