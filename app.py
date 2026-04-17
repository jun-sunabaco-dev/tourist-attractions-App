from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# DB設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spots.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)

# 一覧表示
@app.route('/')
def index():
    return render_template('index.html')

# 登録フォーム表示 & 保存
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        pass  # DB担当のコードが来たら追記
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)