# 1번 섬에서 출발, 다시 1번 섬으로 돌아오는 경로의 모든 경우의 수 


user_input = input() # 섬의 개수
clouds = list(map(int, input().split())) # i번째 섬의 다리 개수
result = 1

for i in clouds:
    result *= i

print(result)