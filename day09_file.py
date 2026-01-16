#"diary.txt"파일을 만들어서, 오늘의 날짜와 농사 일을 기록하는 코드를 짜줘
#한글이 깨지지 않게 해줘
from datetime import datetime
with open("diary.txt", "a", encoding="utf-8") as file:
    today = datetime.now().strftime("%Y-%m-%d")
    file.write(f"{today}: 오늘은 밭에 물을 주고, 잡초를 뽑았다.\n")