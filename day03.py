# day03.py
# 3일차: 편의점 계산기 만들기
cookie_price = 5000 # 과자 가격
drink_price = 1200 # 음료수 가격
my_money = 10000 # 내 지갑 속 돈

# 2. 계산하기 (곱하기, 더하기)
#과자 2개, 음료수 1개 산다면?
total = (cookie_price * 2) + (drink_price * 1)

print("총 결제 금액:", total)

# 3. 거스름돈 계산 (빼기)
change = my_money - total
print("거스름돈:", change)

# 4. 더치페이 계산 (나누기)
# 친구 3명이서 나눠 낸다면?\
dutch_pay = total / 3
print("1인당 낼 돈:", dutch_pay)