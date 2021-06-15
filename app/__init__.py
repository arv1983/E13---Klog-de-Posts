from flask import request, jsonify, render_template, Flask, Blueprint
from environs import Env
from sqlalchemy import Column, Integer, String, DateTime
from flask_sqlalchemy import SQLAlchemy
import psycopg2 
from datetime import datetime


app = Flask(__name__)
env = Env()
env.read_env()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anderson:1234@localhost:5432/e13'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JSON_SORT_KEYS"] = False
db = SQLAlchemy()

class productModel(db.Model):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(300), nullable=False)
    author = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False)

    
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/', methods=["GET"])
def get_create():
    get = productModel()
    all = get.query.all()
    for data in all:
        print(data.id)
    
    return render_template('index.htm', post=all)


@app.route('/api/posts', methods=["POST", "GET"])
def post():
    

    if request.method == "POST":
        data = request.form
        record = {'title': data.get('title'),
        'content':  data.get('content'),
        'author': data.get('author'),
        'email':  data.get('email'),
        'date': datetime.now()}
        print(record)
        try:
            record_db = productModel(**record)
            db.session.add(record_db)
            db.session.commit()
        except:
            return render_template('500.htm')
    
    return render_template('post.htm')


@app.route('/api/posts/<int:post_id>', methods=["GET"])
def post_unique(post_id):
    gets = productModel()
    all = gets.query.filter_by(id=post_id)
    
    return render_template('index.htm', post=all)








