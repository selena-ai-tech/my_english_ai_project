import os
from flask import Flask, request
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from transformers import pipeline
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# Slack Bot 초기화
slack_app = App(token=os.getenv("SLACK_BOT_TOKEN"))
handler = SlackRequestHandler(slack_app)

# Hugging Face 모델 로드
hf_pipeline = pipeline("text2text-generation", model="t5-small")

# Flask 애플리케이션 초기화
app = Flask(__name__)

# Slack 이벤트 처리
@slack_app.event("message")
def handle_message(event, say):
    user_message = event['text']
    
    # Hugging Face API를 사용하여 영어 교정 요청
    response = hf_pipeline(user_message)
    
    # 교정된 메시지 Slack에 전송
    corrected_message = response[0]['generated_text']
    say(text=corrected_message)

# Slack 요청을 Flask와 연결
@app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    app.run(debug=True)
