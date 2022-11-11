# 그래프 공부하기 - defaultdict 자료형으로 양방향 그래프 구현, 그래프 이동하기

from collections import deque # 그래프에서 이동(BFS로 탐색)하기 위해 현재 노드 위치를 관리
from collections import defaultdict # 양방향 인접 리스트 그래프 구현

# 양방향 그래프 구현 - defaultdict
n = 3 # 간선 개수
graph = defaultdict(list) # value에 들어갈 값의 자료형으로 list 지정

for i in range(n):
    s, e = map(int, input().split())
    graph[s].append(e) # 양방향이기 때문에
    graph[e].append(s)

print(graph) # defaultdict(<class 'list'>, {1: [2], 2: [3], 3: [1]})

# 그래프 이동 구현 - queue (BFS로 탐색할 것이기 때문)
q = deque()
q.append(1) # 1번 노드에서 시작
curr = q.popleft() # 현재 노드 위치

q.append(graph[curr]) # 현재 노드와 연결된 노드 리스트를 큐에 추가
next = q.popleft() 

for i in next: # 앞서 추가한 노드 리스트 속 노드들의 정보를 출력, 각각 큐에 추가
    print("%d번 노트에는 %d번 노드로 가는 간선이 있습니다."%(curr, i))
    q.append(i)
#1에는 2가 포함되어 있습니다.
#1에는 3가 포함되어 있습니다.

cur = q.popleft()
print("현재 노드는 %d 입니다."%(cur)) # 현재 노드는 2 입니다.