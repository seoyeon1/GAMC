# 동명이인
# 어떤 이름이 주어질 때, n명의 학생들 중 동명이인의 수


case, pt = input().split() # 학생 수, 어떤 사람의 이름
cnt = 0

s_list = [input() for _ in range(case)] # 학생들 이름 저장

for i in s_list: # 전체 학생들을 대상
    if pt in i: # 자기 이름에 pt이 포함된 경우
        cnt += 1

print(cnt)