# 인덱스 i가 소수인 Ai 값들을 합한 값


n = input()
nums = list(map(int, input().split())) # 주어진 숫자 배열 저장
res = list()

# 함수 : 소수 판별
# 소수 판별 > 주어진 수의 제곱근까지만 비교해도 됨
def isPrime(n):
    if (n == 2):
        return True
    if (n == 1 or n % 2 == 0):
        return False
    for i in range(3, int(n**0.5 + 1), 2): # 3 ~ 제곱근까지 홀수의 약수인지 체크
        if (n % i == 0):
            return False
    return True

for j in range(1, len(nums)+1): # 입력받은 배열을 대상
    if(isPrime(j)): # idx가 소수 > 결과 배열에 추가
        res.append(nums[j-1])

print(sum(res)) # idx가 소수인 원소들의 합