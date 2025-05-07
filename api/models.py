from app import db

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)

    def __repr__(self):
        return f'Movie with title {self.title} & rating {self.rating}'