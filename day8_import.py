# random 라이브러리를 사용해서, 농작물 리스트 중 하나를 추천해주는 코드를 짜줘
import random

crops = ["토마토", "오이", "상추", "당근", "파프리카"]
print("오늘의 추천 농작물은?")
today_pick = (random.choice(crops)) 
print(f"축하합니다! 오늘은 추천 작물은 [{today_pick}] 입니다!")
