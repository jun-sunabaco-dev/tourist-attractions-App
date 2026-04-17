from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spots.db'
app.config['UPLOAD_FOLDER'] = 'static/img/uploads'

db = SQLAlchemy(app)

# Spotモデル（DB設計に合わせる）
class Spot(db.Model):
    __tablename__ = 'spots'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.Text)
    image_path = db.Column(db.Text)
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

# 一覧表示
@app.route('/')
def index():
    spots = Spot.query.all()  # 全件取得
    return render_template('index.html', spots=spots)

# 登録フォーム表示 & 保存
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        category = request.form['category']
        address = request.form['address']

        # 画像の保存
        image = request.files['image']
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))

        # DBに保存
        spot = Spot(
            name=name,
            description=description,
            category=category,
            address=address,
            image_path=image.filename
        )
        db.session.add(spot)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)