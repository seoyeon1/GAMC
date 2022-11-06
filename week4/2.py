# 단풍나무
# 그날 밤에 물들게 될 단풍나무를 바로 업데이트X > 단풍이 모두 물든 곳(0) 정보를 따로 기록 > 기존 단풍 구역에 반영


import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
park = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    trees = list(map(int, input().split()))
    for j in range(1, N + 1):
        park[i][j] = trees[j - 1]
        
def isColored():
    global park, N
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if park[i][j]:
                return 0
    return 1

if isColored():
    print(0)
    exit(0)
        
update = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
day = 1

while 1:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(4):
                ni, nj = i + dy[k], j + dx[k]
                if ni < 1 or nj < 1 or ni > N or nj > N:
                    continue
                if not park[ni][nj]:
                    update[i][j] += 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            park[i][j] = max(0, park[i][j] - update[i][j])
                
    if isColored():
        break

    day += 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            update[i][j] = 0

print(day)