from app import db, app
from app import Article

with app.app_context():
    db.drop_all()
    db.create_all()