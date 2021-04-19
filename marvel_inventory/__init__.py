from flask import Flask
from config import Config

from .Site.routes import site
from .Authenticate.routes import auth
from .Api.routes import api

from flask_migrate import Migrate
from .models import db as root_db, login_manager, ma

from flask_cors import CORS

from.helpers import JSONEncoder

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

root_db.init_app(app)
migrate = Migrate (app, root_db)

login_manager.init_app(app)
login_manager.login_view = 'auth.signin' 

ma.init_app(app)

CORS(app)

app.json_encoder = JSONEncoder

from marvel_inventory import models