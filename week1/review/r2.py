# 1주차 2번 다시풀기

# [문제해설] - 문자열 매칭, 반복문
# 출력 : n개의 문자열 > 문자열 s를 포함한 문자열 개수
# 자신의 이름을 포함한 사람이 모두 몇 명 있는지

# python의 String메소드, 반복문으로 해결


# [정답풀이]
n, s = input().split() # 본인 제외 사람들 수, 자기 이름
cnt = 0

for i in range(int(n)):
    name = input()
    if s in name: # 자신의 이름을 포함한 사람이라면
        cnt += 1

print(cnt)