import os
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from forms import AddForm, UpdateForm, DeleteForm

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


@app.route('/add', methods=['GET', 'POST'])
def add_page():
    form = AddForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        featured = form.featured.data
        # Add new post to database
        post = Post(title, content, featured)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add-page.html', form=form)


@app.route('/article/<id>')
def article_page(id):
    post = Post.query.get(id)
    posts = Post.query.all()
    return render_template('article-page.html', post=post, posts=posts)


@app.route('/search')
def search_results_page():
    return render_template('search-results-page.html')


@app.route('/update/<id>', methods=['GET', 'POST'])
def update_page(id):
    form = UpdateForm()
    post = Post.query.get(id)
    posts = Post.query.all()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.featured = form.featured.data
        db.session.commit()
        return redirect(url_for('index'))

    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.featured.data = post.featured

    return render_template('update-page.html', post=post, posts=posts, form=form)


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete_page(id):

    form = DeleteForm()

    if form.validate_on_submit():
        id = form.id.data
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.id.data = id
    return render_template('delete-page.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
