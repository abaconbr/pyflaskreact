from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__,template_folder="templates",static_folder="static",static_url_path="/backend/static")
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text())
    due = db.Column(db.DateTime, default = datetime.now)
    
    def __init__(self, title, body):
        self.title = title
        self.body = body

if os.path.exists('./instance/todo.db'):
    print('todo.dbが存在ですから作成不要です')
else:
    with app.app_context():
        db.create_all()

class ArticleSchema(ma.Schema):
    class  Meta:
        fields = ('id', 'title', 'body', 'due')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
  return render_template('index.html')

@app.route('/api/get', methods = ['GET'])
def get_article():
    all_articles = Articles.query.all()
    results = articles_schema.dump(all_articles)
    return jsonify(results)

@app.route('/api/get/<id>', methods = ['GET'])
def post_details(id):
    article = Articles.query.get(id)
    return article_schema.jsonify(article)

@app.route('/api/add', methods = ['POST'])
def add_article():
    title = request.get_json().get('title')
    body = request.get_json().get('body');
    article = Articles(title=title, body=body)
    db.session.add(article)
    db.session.commit()
    return article_schema.jsonify(article)

@app.route('/api/update/<id>', methods=['PUT'])
def update_article(id):
    article = Articles.query.get(id)
    title = request.get_json().get('title')
    body = request.get_json().get('body');
    
    article.title = title
    article.body = body
    db.session.commit()
    return article_schema.jsonify(article)

@app.route('/api/delete/<id>', methods = ['DELETE'])
def delete_article(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return article_schema.jsonify(article)

if __name__ == '__main__':
    app.run(debug=True)
