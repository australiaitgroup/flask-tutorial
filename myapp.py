import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

# SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Post(db.Model):

    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    featured = db.Column(db.Boolean, default=True, nullable=False)
    create_Date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, title, content, featured):
        self.title = title
        self.content = content
        self.featured = featured

    def __repr__(self):
        return f"This post's title is {self.title}."


############################################

        # VIEWS WITH FORMS

##########################################


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('home-page.html', posts=posts)


@app.route('/add')
def add_page():
    return render_template('add-page.html')


@app.route('/article')
def article_page():
    return render_template('article-page.html')


@app.route('/search')
def search_results_page():
    return render_template('search-results-page.html')


@app.route('/update')
def update_page():
    return render_template('update-page.html')


if __name__ == '__main__':
    app.run(debug=True)
