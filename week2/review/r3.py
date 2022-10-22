# 2주차 3번 다시풀기

# [문제해설] - 정렬, 문자열
# 출력 : 4개의 정수 > 맨허튼 거리가 가장 긴 경우 찾기
# key가 2개 이상일 때 정렬 : 1. 이름(사전순) > 2. 동명이인 경우, 키(오름차순)


# [정답 풀이]
n, k = map(int, input().split())
arr = []

for i in range(n): # 출석부에 학생 정보 저장
    name, tall = input().split()
    arr.append([name, tall])

arr = sorted(arr, key = lambda x : (x[0], x[1])) # key가 2개일 때 정렬
print(arr[k-1][0], arr[k-1][1])
