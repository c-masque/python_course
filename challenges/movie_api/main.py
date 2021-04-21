'''
Fully CRUD'ded out API with flask and a sqlite db.
Your Schema should include at least:
- id 
- title
- rating
- leading_role
- release_date

Model needs to reflect all fields in the db.

All of the routes should be tested in Postman whitout issue before sending to me.

Work up to Flask's render_template method to create a UI
'''

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

db = SQLAlchemy(app)
ma = Marshmallow(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False)
    content = db.Column(db.String(1000), unique=False)
    rating = db.Column(db.String(3))
    leading_role = db.Column(db.String(30))
    release_year = db.Column(db.String(4))

    def __init__(self, title, content, rating, leading_role, release_year):
        self.title = title
        self.content = content


class MovieSchema(ma.Schema):
    class Meta:
        fields = ('title', 'content', 'rating', 'leading_role', 'release_year')


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

## ROUTES BELOW ##

@app.route("/api")
def home():
    return "This is the root"

@app.route("/new-movie-entry", methods=['POST'])
def add_movie():

    title = request.json['title']
    content = request.json['content']
    rating = request.json['rating']
    leading_role = request.json['leading_role']
    release_year = request.json['release_year']

    new_movie_entry = Movie(title, content, rating, leading_role, release_year)
    db.session.add(new_movie_entry)
    db.session.commit()

    movie_entry = Movie.query.get(movie_entry.id)

    # THIS RETURN IS SUPER BROKEN
    return movie_schema.jsonify(movie_entry) # FIX FIX FIX


if __name__ == "__main__":
    app.run(debug=True)