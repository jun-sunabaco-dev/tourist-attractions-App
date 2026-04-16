from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        pass  # DB担当のコードが来たら追記
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)