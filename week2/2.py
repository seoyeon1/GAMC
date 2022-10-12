# 철자 분리 집합
# 주어진 기준에 따라 문자열을 분리 > 분리된 개수(분리 집합) 출력


n = int(input())
text = input()

cnt = 1 # 부분집합 개수
tmp = [text[0]] #  같은 집합인지 판단하는 기준 문자 배열

for i in text[1:]:
    if(tmp[-1] != i): # 기준문자와 다른 문자라면 다른 집합
        cnt += 1
        tmp.append(i) # 기준문자 교체


print(cnt)