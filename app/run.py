# run.py

from app import app
from models import db  # Import the db instance from models

from routes import home


# @app.route('/')
# def index():
#     return hello()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Starting the Flask app with app.run")
    app.run(debug=True)
