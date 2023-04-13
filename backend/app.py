from datetime import datetime, date, time
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    detail = db.Column(db.String(100))
    due = db.Column(db.DateTime, nullable=False)

if os.path.exists('./instance/todo.db'):
    print('todo.dbが存在ですから作成不要です')
else:
    with app.app_context():
        db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', token="hello Flask+React")
'''
    if request.method == 'GET':
        posts = Post.query.order_by(Post.due).all()
        return render_template('index.html', posts=posts, today=date.today())
    else:
        title = request.form.get('title');
        detail = request.form.get('detail');
        due = request.form.get('due');
        due = datetime.strptime(due, '%Y-%m-%d');
        new_post = Post(title=title, detail=detail, due=due)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
'''
@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/detail/<int:id>')
def read(id:int):
    post = Post.query.get(id)
    return render_template('detail.html', post=post)

@app.route('/delete/<int:id>')
def delete(id:int):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id:int):
    post = Post.query.get(id)

    if request.method == 'GET':
        print("is me");
        return render_template('update.html', post=post)
    else:
        post.title = request.form.get('title')
        post.detail = request.form.get('detail')
        post.due = datetime.strptime(request.form.get('due'), '%Y-%m-%d')
        db.session.commit()
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=9000)
