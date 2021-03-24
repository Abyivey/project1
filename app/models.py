from . import db


class PropertyInfo(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key = True, unique = True)
    title = db.Column(db.String(225))
    num_bedrooms = db.Column(db.String(25))
    num_bathrooms = db.Column(db.String(25))
    location = db.Column(db.String(225))
    price = db.Column(db.String(225))
    typeHA = db.Column(db.String(25))
    description = db.Column(db.String(225))
    photo = db.Column(db.String(225))

    def __init__(self, title, num_bedrooms, num_bathrooms, location, price, typeHA, description, photo):
        self.title = title
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.location = location
        self.price = price
        self.typeHA = typeHA
        self.description = description
        self.photo = photo
    
    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)


