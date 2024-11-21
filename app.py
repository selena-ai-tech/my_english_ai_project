import os
from slack_bolt import App
from flask import Flask, request
import requests

# 환경 변수 가져오기
slack_bot_token = os.environ.get("SLACK_BOT_TOKEN")
slack_signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
huggingface_api_key = os.environ.get("HUGGINGFACE_API_KEY")

# Slack Bolt 앱 초기화
slack_app = App(
    token=slack_bot_token,
    signing_secret=slack_signing_secret,
)

# Flask 앱 초기화
flask_app = Flask(__name__)

@slack_app.event("app_mention")
def handle_mention(event, say):
    say("안녕하세요! 무엇을 도와드릴까요?")

@flask_app.route("/huggingface", methods=["POST"])
def huggingface_request():
    data = request.json
    headers = {"Authorization": f"Bearer {huggingface_api_key}"}
    response = requests.post("https://api-inference.huggingface.co/models/gpt2", headers=headers, json=data)
    return response.json()

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return slack_app.dispatch(request)

if __name__ == "__main__":
    flask_app.run(port=3000)
