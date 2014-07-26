from flask import g, render_template, redirect
from flask.ext.login import current_user, logout_user
from . app import app, login_manager
from . models import User


@app.before_request
def set_g_user():
    g.user = current_user._get_current_object()


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
    return render_template('index.html', user=g.user)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')
