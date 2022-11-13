# 개미와 진딧물

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

n, k = map(int, input().split())
list_1 = list()
list_2 = list()
for i in range(n):
    tmp = list(map(int, input().split()))
    for s in range(n):
        if tmp[s] == 1:
            list_1.append([i, s])
        elif tmp[s] == 2:
            list_2.append([i, s])

cnt = 0
for pos1 in list_1:
    idx = 0
    while True:
        if idx == len(list_2):
            break
        pos2 = list_2[idx]
        if manhattan(pos1, pos2) <= k:
            cnt += 1
            break
        else:
            idx += 1
print(cnt)