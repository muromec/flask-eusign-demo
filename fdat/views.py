from flask import g, render_template
from flask.ext.login import current_user
from . app import app, login_manager
from . models import User


@app.before_request
def set_g_user():
    g.user = current_user


@login_manager.user_loader
def load_user(userid):
    print 'ya load user', userid
    try:
        return User.query.get(int(userid))
    except (TypeError, ValueError):
        pass


@app.route('/')
def index():
    print g.user
    return render_template('index.html')
