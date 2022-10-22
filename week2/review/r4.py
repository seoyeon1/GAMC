# 2주차 4번 다시풀기

# [문제해설] - 2차원 배열 탐색
# 출력 : 2차원 배열 > 배열 내의 모든 폭탄값의 합
# 폭탄 터짐 : 2차원 배열에서 한 지점(좌표)을 기준으로 상하좌우 탐색 > 방향좌표(dx,dy) 이용
# deque 사용해서 구현(collections)


# [정답 풀이]
import sys
input = sys.stdin.readline
from collections import deque
dx = [0 ,0, 1, -1]
dy = [1, -1, 0, 0]

n, k = map(int, input().split())
mat = [[ 0 for _ in range(n)] for _ in range(n)] # 0으로 초기화된 n*n 2차원 배열

q = deque()
for _ in range(k): # 폭탄이 떨어질 위치들 저장
    s, e = map(int ,input().split())
    q.append([s-1, e-1])

while q:
    x, y = q.popleft() # 폭탄이 터진 지점의 좌표
    mat[x][y] += 1
    for i in range(4): # 상하좌우에 폭탄 영향주기
        nx = x + dx[i]
        ny = y + dy[i]
        if 0  <= nx < n and 0 <= ny < n: # 주어진 공간(idx값)을 벗어나지 않을 때만 영향 적용
            mat[nx][ny] += 1

ans = 0 # 모든 폭탄값의 합
for i in mat:
    ans += sum(i)
print(ans)