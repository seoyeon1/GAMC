# 철자 분리 집합


n = int(input())
text = input()

cnt = 1
tmp = [text[0]]

for i in text[1:]:
    if(tmp[-1] != i):
        cnt += 1
        tmp.append(i)


print(cnt)