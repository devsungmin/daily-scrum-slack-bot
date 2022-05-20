import json
import requests
from datetime import datetime


def send_message(send_msg, channel_name):
    TOKEN = json.loads(open('secret_key.json').read())["SLACK_NOTIFY"]["BOT_USER_OAUTH_TOKEN"]
    URL = "https://slack.com/api/chat.postMessage"

    try:
        response = requests.post(URL,
                                 headers={"Authorization": "Bearer " + TOKEN},
                                 data={"channel": channel_name, "text": send_msg}
                                 )
    except Exception as e:
        send_msg = '🚨 Error 🚨 \n ' + str(e)
        response = requests.post(URL,
                                 headers={"Authorization": "Bearer " + TOKEN},
                                 data={"channel": channel_name, "text": send_msg}
                                 )
    print(response)


if __name__ == '__main__':
    today = datetime.now().strftime('%Y-%m-%d')
    channel_name = "#00-1조-디프만-1번출구-데일리스크럼"
    message = f' 📢 {today} 데일리 스크럼 시간입니다. 📢 \n' \
              "✅ 오늘 할 일 ✅\n" \
              "❗️ highest ❗️\n" \
              "- \n\n" \
              "‼️ high ‼️\n" \
              "- \n\n" \
              "어떤 장애물이나 문제가 있나요?\n" \
              "- \n\n" \
              "🕰 오늘의 집중 타임 🕰" \
              "ex) AM 09:00 ~ PM 20:00"\

    send_message(message, channel_name)
