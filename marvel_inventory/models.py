from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime

#Adding Flask security for paswords 
from werkzeug.security import generate_password_hash, check_password_hash

#import for secrets module (provided by python)
import secrets

#Imports for Login Manager and teh Usermixin
from flask_login import LoginManager, UserMixin

#Import for flask-marshmello
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = False, default = '')
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    drone = db.relationship('Drone', backref = 'owner', lazy = True)

    def __init__(self, email, first_name = '', last_name = '', id = '', password = '', token = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'user {self.email} has been created and added to the data base!'

class Character(db.Model):
    id = db.Column(db.String, primary_key = True)
    real_name = db.Column(db.String(150))
    alias = db.Column(db.String(150))
    description = db.Column(db.String(200))
    power = db.Column(db.String(200))
    first_appearence = db.Column(db.String(150))
    affliation = db.Column(db.String(100))
    living_status= db.Column(db.String(100))
    citizenship = db.Column(db.String(100))
    martial_status = db.Column(db.String(50))
    occupation = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    height = db.Column(db.String(150))
    weight = db.Column(db.String(150))
    place_of_birth = db.column(db.String(150))
    creators = db.Column(db.String(150))
    user_token= db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self,real_name,alias,description,power,first_appearence,affliation,living_status,citizenship,marital_status,occupation,gender,height,weight,place_of_birth,creators,user_token = user_token ):
        self.id = self.set_id()
        self.real_name = real_name
        self.alias = alias
        self.description = description 
        self.power = power
        self.first_appearence = first_appearence
        self.affliation = affliation
        self.living_status = living_status
        self.citizenship = citizenship
        self.martial_status = marital_status
        self.occupation = occupation
        self.gender = gender
        self.height = height
        self.weight = weight
        self.place_of_birth = place_of_birth
        self.creators = creators
        self.user_token = user_token
def __repr__(self):
    return f'The following charactor has been added:{self.real_name}'

def set_id(self):
    return (secrets.token_urlsafe()) 


#creation of api schema via the marshmallo package
class CharacterSchema(ma.Schema):
    class Meta:
        fields = ['id', 'real_name','alias','description','power','first_appearence','affliation','living_status','citizenship','marital_status','occupation','gender','height','weight','place_of_birth','creators']


character_schema = CharacterSchema()
characters_schema = CharacterSchema(many = True)
