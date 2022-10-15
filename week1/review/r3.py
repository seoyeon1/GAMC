# 1주차 3번 다시풀기

# [문제해설] - 탐색
# 출력 : 4개의 정수 > 맨허튼 거리가 가장 긴 경우 찾기
# 완전탐색으로 모든 조합을 비교해 찾을 수도 있지만
# 4개의 정수를 크기순 정렬 > (a, a+b), (a+c, a+d) / (a, a+b), (a+d, a+c)일 때 c + d - b로 최장 거리 가능

# [수학적 개념] - 맨허튼 거리
# 맨허튼 거리 : |x1-x2| + |y1-y2| , 좌표평면에서 거리측정법


# [정답 풀이]
import sys
input = sys.stdin.readline

arr = list(map(int, input().split())) # 파일에서 읽어온 값을 공백기준으로 나누기 & int변환 후 리스트에 저장
arr.sort() # 오름차순 정렬

x = abs(arr[0]-arr[3]) # 맨허튼 거리 계산
y = abs(arr[1]-arr[2])

print(x + y)