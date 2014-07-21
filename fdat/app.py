from flask import Flask
from flask.ext.login import LoginManager
from social.apps.flask_app.routes import social_auth
from social.apps.flask_app.models import init_social

from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('../local.cfg', silent=True)
app.config.from_pyfile('config.py')

app.register_blueprint(social_auth)

login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)
init_social(app, db)

