from flask import Flask, render_template
# Flaskのインポート

app = Flask(__name__)
# アンダーバー2つ

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ja")
def hello():
    return "<p>こんにちは</p>"
# /ja/というURLにアクセスしたら、"こんにちは"を返す

@app.route("/temptest")
def temptest():
    return render_template("index.html")
# htmlをリンクさせて読み込み

if __name__=="__main__":
    app.run(debug=True)