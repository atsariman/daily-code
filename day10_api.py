# requests 라이브러리를 사용하여 Open-Meteo 무료 API로
# 제주도 (위도 33.49, 경도 126.53)의 현재 날씨와 기온을 가져와서 출력해줘
import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=33.49&longitude=126.53&hourly=temperature_2m,relativehumidity_2m"

print("날씨 서버 접속중...")
response = requests.get(url)
data = json.loads(response.text)
if response.status_code == 200:
    current_temp = data['hourly']['temperature_2m'][0]
    current_humidity = data['hourly']['relativehumidity_2m'][0]
    print(f"현재 제주도의 기온은 {current_temp}°C, 습도는 {current_humidity}% 입니다.")
else:
    print("날씨 정보를 가져오는데 실패했습니다.")