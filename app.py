import os
from slack_bolt import App

slack_token = os.getenv("SLACK_BOT_TOKEN")  # 환경 변수에서 토큰 가져오기

# SLACK_BOT_TOKEN이 없으면 오류를 발생시킬 수 있으므로 추가적인 오류 처리도 가능
if not slack_token:
    raise ValueError("SLACK_BOT_TOKEN is not set. Please set the environment variable.")

# Slack 앱 초기화
slack_app = App(token=slack_token)
# Hugging Face API Key 가져오기
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")  # GitHub Secrets에서 가져옴

# Slack App 초기화
slack_app = App(token=slack_bot_token, signing_secret=slack_signing_secret)

# Slack App 기능 추가 (예제)
@slack_app.event("app_mention")
def handle_app_mention(event, say):
    say("Hello! I'm your Slack bot.")

# Hugging Face API 사용 예제
def use_huggingface_api(text):
    import requests

    url = "https://api-inference.huggingface.co/models/distilgpt2"
    headers = {"Authorization": f"Bearer {huggingface_api_key}"}
    response = requests.post(url, headers=headers, json={"inputs": text})
    return response.json()

# Flask 서버 실행 (필요한 경우)
if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Slack Bot is running!"

    app.run(host="0.0.0.0", port=5000)
