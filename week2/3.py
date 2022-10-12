# 출석부
# n명의 학생들 중 k번째 학생의 이름, 키 출력
# 정렬(오름차순) : 이름 > 키 

# [나의 풀이]
# [1차] - dict() 이용 (이름 : 키) 정보 저장 > 테스트는 통과, 제출 실패
# 이유 : 동명이인인 경우, dict 객체는 값 추가 X 기존 이름의 값을 변경시키는 문제 발생

# [2차] - list() 이용 > 제출 성공


n, k = map(int, input().split())

# [1차 풀이]
# book = {}

# for i in range(n):
#     name, tall = input().split()
#     book[name] = tall
# print(book)
# sorted(book.items(), key= lambda x : x[1]) 
# print(list(list(book.items())[k-1])[0], list(list(book.items())[k-1])[1])


# [2차 풀이]
book = []

for i in range(n):
    name, tall = input().split()
    book.append([name, tall])

book = sorted(book, key = lambda x : (x[0], x[1])) # 정렬 기준 1. 이름 > 동명이인 > 2. 키
print(book[k-1][0], book[k-1][1])