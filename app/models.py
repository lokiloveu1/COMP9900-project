from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_host = db.Column(db.Boolean())
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    listings = db.relationship('Accommodation', backref='host', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Accommodation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(120))
    num_guests = db.Column(db.Integer, nullable=False)
    num_bedrooms = db.Column(db.Integer, nullable=False)
    num_beds = db.Column(db.Integer, nullable=False)
    num_bathrooms = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    suburb = db.Column(db.String(32), nullable=True)
    city = db.Column(db.String(32), nullable=False)
    state = db.Column(db.String(32))
    country = db.Column(db.String(32), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    property_type = db.Column(db.String(32), nullable=False)
    amenities = db.Column(db.Text)
    rating = db.Column(db.Float)
    num_reviews = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Accommodation {}>'.format(self.name)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accommodation_id = db.Column(db.Integer, db.ForeignKey('accommodation.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(32), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accommodation_id = db.Column(db.Integer, db.ForeignKey('accommodation.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text)

