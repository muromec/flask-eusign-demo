from fdat.views import app
from fdat.app import db

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
