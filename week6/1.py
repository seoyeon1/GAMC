# 7게임

# [문제해설] - 문자열, 사칙연산
# 길이가 7인 문자열 ABCDEFG > 홀수 번째 : A, C, E, G, 짝수 번째 : B, D, F
# 문자열 슬라이싱, 반복문으로 해결

# [유형] - 문자열 : 입력값의 범위를 고려
# 1. 자료형 변환 : 문자열 -> 숫자 > 2. 전체에서 특정 문자열의 존재, 위치 파악 / 추가 조건 적용하는 유형


# [정답풀이] - [방법1]
import sys
input = sys.stdin.readline

for _ in range(5):
    arr = list(input().rstrip())
    chk = 0
    for i in range(0, 7, 2): # 홀수만
        chk += int(arr[i])

    for i in range(1, 7, 2): # 짝수만
        if int(arr[i]) != 0: # 0을 곱하지 않도록 체크
            chk *= int(arr[i])

    print(chk % 10)


# [방법2]
for _ in range(5):
    string  = input().rstrip()
    total = int(string[0]) + int(string[2])  + int(string[4]) + int(string[6])

    if string[1] != "0":
        total *= int(string[1])
    if string[3] != "0":
        total *= int(string[3])
    if string[5] != "0":
        total *= int(string[5])
    print(total % 10)