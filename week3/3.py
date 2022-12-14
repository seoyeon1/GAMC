# 구름이의 여행

# [문제해설] - 그래프, bfs
# 출력 : 양방향 그래프 > 1번 섬(노드)에서 N번 섬(노드)까지 K개 이하의 다리만 건너서 갈 수 있는지 판단

# [정답 풀이]
import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict

n, m, k = map(int, input().split())
dict = defaultdict(list)
for i in range(m):
    s, e = map(int, input().split())
    dict[s].append(e)
    dict[e].append(s)

q = deque()
#
visited = [-1 for _ in range(n+1)]
visited[1] = 0

q.append(1)
while q:
    cur = q.popleft()
    for next in dict[cur]:
        if visited[next] != -1:
            continue
        q.append(next)
        visited[next] = visited[cur] + 1
if 1 <= visited[n] <= k:
    print("YES")
else:
    print("NO")