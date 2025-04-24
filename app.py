from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'こんにちは。これは Render で実行されているテスト アプリです。'
