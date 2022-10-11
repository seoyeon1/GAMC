# 폭탄 터트리기
# 폭탄값 : 폭탄 터짐 > 해당 위치(+1)로 상하좌우 위치도 영향 받음(+1)
# 전체 영역(n*n)에 k개의 폭탄이 터졌을 때 > 전체 영역의 폭탄값 합계 구하기

# 나의 풀이
# 2차원 배열 생성 > dx, dy : 방향좌표 배열을 활용 > for문 : 폭발 위치에 접근 > sum() : 전체 폭탄값 계산


n, k = map(int, input().split())
bomb = []

for _ in range(k): # 폭파 지점들 저장
    bomb.append(list(map(int, input().split())))
# print(bomb)

ground = [[0]*n for _ in range(n)] # 전체 영역인 2차원 배열 생성
# 방향좌표 배열 - 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 폭탄값 증가
for i in bomb: 
    ground[i[0]-1][i[1]-1] += 1 # 폭파 지점 

    for x in range(4): # 상하좌우 위치
        nx = i[0]-1 + dx[x]
        ny = i[1]-1 + dy[x]
        if nx < 0 or ny < 0 or nx > n-1 or ny > n-1: # 전체 영역을 벗어나지 않도록
            continue
        ground[nx][ny] += 1

result = 0
for k in ground:
    result += sum(k)

print(result)