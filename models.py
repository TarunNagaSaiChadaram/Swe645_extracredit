# - Samanvitha Matta (G01252738)
# - Akshaya Reddy Dundigalla (G01482843)
# - Tarun Naga Sai Chadaram (G01445928)
#The StudentSurvey model is defined using SQLAlchemy ORM.
# Shows the'studsurvectab' table, which contains the data from the student survey.

from database import db

class StudentSurvey(db.Model):
    __tablename__ = 'studsurvectab'  

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    street_address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    campus_likes = db.Column(db.Text, nullable=True)
    campus_interests = db.Column(db.Text, nullable=True)
    recommend = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "street_address": self.street_address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "phone": self.phone,
            "email": self.email,
            "campus_likes": self.campus_likes,
            "campus_interests": self.campus_interests,
            "recommend": self.recommend
        }
