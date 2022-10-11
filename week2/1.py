# 출석부
# 이름 오름차순 > 키 오름차순

n, k = map(int, input().split())
book = {}

for i in range(n):
    name, tall = input().split()
    book[name] = tall
sorted(book.items(), key= lambda x : x[1]) # 이름이 같을 때 > 키 오름차순

print(list(list(book.items())[k-1])[0], list(list(book.items())[k-1])[1])