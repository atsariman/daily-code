import matplotlib.pyplot as plt
import numpy as np

# 데이터 설정 (소스 [1] 기반)
categories = [
    '유효 인산', '잠재적 가용 질소', '철', '아연', '칼슘', 
    'CEC', '마그네슘(1)', '유기물', '구리', '총 탄소', '칼륨'
]

# 2024년 데이터 (pH 65는 그래프 왜곡을 피하기 위해 제외하거나 6.5로 수정 필요)
values_2024 = [278, 141, 149, 93.6, 58, 38, 21.1, 12.7, 9.5, 7.4, 6.3]
# 2025년 데이터
values_2025 = [257, 110, 148, 66.2, 55, 38, 18.8, 10.6, 10.3, 6.1, 7.1]

x = np.arange(len(categories))  # 항목 위치
width = 0.35  # 막대 너비

# 그래프 그리기 설정
fig, ax = plt.subplots(figsize=(14, 8))
rects1 = ax.bar(x - width/2, values_2024, width, label='2024', color='#87CEFA') # 하늘색
rects2 = ax.bar(x + width/2, values_2025, width, label='2025', color='#FF6F61') # 산호색

# 레이블 및 제목 설정
ax.set_ylabel('성분 수치')
ax.set_title('5373-B1 토양 분석 비교 (2024 vs 2025)')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45)
ax.legend()

# 막대 위에 값 표시
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.show()