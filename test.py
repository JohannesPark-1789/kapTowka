import requests
import schedule
import time

# 카카오톡 API 토큰
KAKAO_TOKEN = 'YOUR_KAKAO_API_TOKEN'

# 메시지 전송 함수
def send_message(user_id, message):
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
    headers = {
        'Authorization': f'Bearer {KAKAO_TOKEN}'
    }
    data = {
        'object_type': 'text',
        'text': message,
        'link': {
            'web_url': 'http://www.example.com',
            'mobile_web_url': 'http://www.example.com'
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Message sent to {user_id} successfully.")
    else:
        print(f"Failed to send message to {user_id}: {response.status_code}")

# 스케줄링 설정 함수
def schedule_message(user_id, message, time):
    schedule.every().day.at(time).do(send_message, user_id, message)

# 사용자 정보와 메시지
user_id = 'USER_ID'
message = 'Hello! This is your scheduled message.'

# 매일 특정 시간에 메시지 전송
schedule_message(user_id, message, '12:00')

while True:
    schedule.run_pending()
    time.sleep(1)
