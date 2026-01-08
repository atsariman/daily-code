# 작물 이름과 무게(kg)를 넣으면 총 가격을 계산해주는 함수를 만들어줘
# 가격표: 콩 1000원, 감귤 2000원      
def calculate_price(name, weight):
    price_list = {
        "콩": 1000,
        "감귤": 2000
    }
    
    if name in price_list:
        total_price = price_list[name] * weight
        return total_price
    else:
        return "해당 작물의 가격 정보를 찾을 수 없습니다."   
    
    # 2. 기계 사용하기 (함수 호출)
print("--- 🤖 자동 계산기 가동 ---")

total1 = calculate_price("콩", 3)
print(f"손님 1: 콩 3kg 가격은 {total1}원 입니다.")

total2 = calculate_price("감귤", 5)
print(f"손님 2: 감귤 5kg 가격은 {total2}원 입니다.")