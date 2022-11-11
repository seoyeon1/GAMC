from collections import deque
from collections import defaultdict

graph = defaultdict(list)
N, M = map(int, input().split())
visited = [0 for _ in range(N)] # 방문 여부(1) 체크 (재방문 X 때문에)

# 양방향 그래프 구현
for i in range(M): 
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 현재 노드 위치를 관리(방문 순서대로 출력)
q = deque()
q.append(0)

while q:
    cur = q.popleft()
    visited[cur] = 1
    print("현재 위치는 %d 입니다."%(cur))

    for i in graph[cur]:
        if visited[i] == 0: # 한번도 방문한 적이 없다면 > 검색을 위해 큐에 추가
            q.append(i)

'''
result
현재 위치는 0 입니다.
현재 위치는 1 입니다.
현재 위치는 2 입니다.
현재 위치는 5 입니다.
현재 위치는 4 입니다.
현재 위치는 6 입니다.
현재 위치는 3 입니다.
'''
