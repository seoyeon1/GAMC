# 최장 맨허튼 거리
# 맨허튼 거리 : |x1-x2|+|y1-y2|
# 정수 4개를 2개씩 짝을 지어 좌표로 표현 > 최장 맨허튼 거리 계산
# !! 입력 순서대로 x1 ~ y2가 아님


nums = list(map(int, input().split()))
nums = sorted(nums) # 두 점 사이의 거리 최대 > 정렬!

print(abs(nums[0]-nums[2]) + abs(nums[1]+nums[3])) # 맨허튼 거리 계산