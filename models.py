from marshmallow import Schema, fields

from setup_db import db


class Movie(db.Model):
    """
    Создание класса Movie.
    """
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)

    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")

    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    """
    Создание схемы MovieSchema.
    """
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()

    director_id = fields.Int()
    genre_id = fields.Int()

    director = fields.Pluck("DirectorSchema", "name")
    genre = fields.Pluck("GenreSchema", "name")


class Director(db.Model):
    """
    Создание класса Director.
    """
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    """
    Создание схемы DirectorSchema.
    """
    id = fields.Int()
    name = fields.Str()


class Genre(db.Model):
    """
    Создание класса Genre.
    """
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """
    Создание схемы GenreSchema.
    """
    id = fields.Int()
    name = fields.Str()
