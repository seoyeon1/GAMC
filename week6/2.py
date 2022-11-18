# 제곱암호

# [문제해설] - 문자열 처리, 조건문
# 문자열(문숫문숫...) > 조건에 따라 문자열 변환(재구성)하는 유형
# 문자열 > 숫자와 문자로 나눠서 변환, 각각 계산


# [정답풀이]
import sys
import string

alpha_small = list(string.ascii_lowercase)
input = sys.stdin.readline
n = int(input())
arr = list(input().rstrip()) # 문자열 오른쪽 공백 제거
res = ''

for i in range(0, n, 2): # 문자, 숫자 분리
	ch = arr[i]
	num = int(arr[i+1])
	index = (alpha_small.index(ch) + (num * num))%26 # 변환한 알파벳 인덱스
	res += alpha_small[index]

print(res)