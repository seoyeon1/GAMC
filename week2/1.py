# 합격자 찾기

# [2주차 후기]
# goorm에서 `기본으로 제공되는 입력을 받는 코드`가 아직 익숙치 않아서 이번주도 py로 풀었지만 다음엔 js로 풀 수 있도록/ 복습할 때 기존 문제를 js로 풀어봐야겠다
# 주어진 문제에 맞춰서 입력 받는 부분을 수정해풀어보도록
# 파이썬 안쓴지 2달 정도 된 거 같은데 그래서 지금 문법적으로 js처럼 쓰게 될 때도 있고 전이었다면 빨리 풀었을 것도 가물가물해진 상태 잊지않도록 둘 다 해보자


import sys
input = sys.stdin.readline # 시험 정보 입력받기

student = list()
score = list()
test = int(input())

# 시험 정보 저장
for i in range(test): 
    student.append(int(input())) # 응시 학생 수
    score.append(list(map(int, input().strip().split()))) # 점수들

# 문제 별 합격자수/응시학생수 계산
for i in range(len(student)): 
    mean = sum(score[i])/student[i]
    ok = len(list(filter(lambda v : v >= mean, score[i]))) # 합격한 점수만 필터링
    print(f"{ok}/{student[i]}")