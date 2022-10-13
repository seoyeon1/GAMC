# 1번 섬에서 출발, 다시 1번 섬으로 돌아오는 경로의 모든 경우의 수 


user_input = input() # 섬의 개수
clouds = list(map(int, input().split())) # i번째 섬의 다리 개수
result = 1

for i in clouds:
    result *= i

print(result)


# [문제해설] - 경우의 수
# 출력 : 1번 섬에서 모든 섬을 돌아 다시 1번 섬으로 돌아오는 경우의 수
# 섬으로 이동 > 하나의 독립 사건

# [수학적 개념] - 합의 법칙, 곱의 법칙
# 합의 법칙 : 독립사건A 또는 B가 일어나는 경우. 두 경우의 수를 합치면 됨
# 곱의 법칙 : 독립사건 A와 B가 동시에 일어나는 경우의 수. 경우의 수를 모두 곱하면 됨

# [정답 풀이]
N = int(input()) # 섬의 개수
ans = 1
B = list(map(int, input().split())) # 다리 수 배열
for i in B:
    ans = ans * i # 곱의 법칙 적용

print(ans)