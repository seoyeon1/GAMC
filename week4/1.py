# 체크카드
# 예약 기능 구현 > 큐 사용 > 처음엔 else에 만들었지만 실패 케이스 존재(pay일 때, 잔고 부족인 경우도 else에 포함되기 때문) > elif로 명시, 입금 후 체크하는 방식으로 진행
from collections import deque

now, m = map(int, input().split())
Q = deque()

for _ in range(m):
	req, money = input().split()
	money = int(money)
		
	if req == 'deposit': # 입금
		now += money
		# 입금 진행 후, 큐에 값이 있고 값을 처리할 수 있을만한 잔고가 있을 때까지 예약한 결제 진행
		while Q and now >= Q[0]:
			now -= Q[0]
			Q.popleft() 
		# print(now, req, money)	
	elif req == 'pay' and now >= money: # 결제 : 충분한 잔고가 있을 때만
		now -= money
		# print(now, req, money)
	elif req == 'reservation': # 결제 대기 : 잔고가 부족하면 대기큐에 추가
		if not Q and now >= money:
			now -= money
		else:
			Q.append(money)
		# print(now, req, money)		
print(now)