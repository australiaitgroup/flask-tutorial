import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
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


# class Tutor(db.Model):

#     __tablename__ = 'tutors'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text)
#     company = db.relationship('Company', backref='tutor', uselist=False)

#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         if self.company:
#             return f"Tutor name is {self.name} and company is {self.company.name}"
#         else:
#             return f"Tutor name is {self.name} and has no company assigned yet."


# class Company(db.Model):

#     __tablename__ = 'companies'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text)
#     # We use tutors.id because __tablename__='tutors'
#     tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id'))

#     def __init__(self, name, tutor_id):
#         self.name = name
#         self.tutor_id = tutor_id

#     def __repr__(self):
#         return f"Company Name: {self.name}"
############################################

        # VIEWS WITH FORMS

##########################################


@app.route('/')
def index():
    return render_template('home-page.html')

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
