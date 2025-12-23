from datetime import datetime
from models import db

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    password=db.Column(db.String(50), nullable=False)
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    def __repr__(self):
        return f"<User id={self.id}, email={self.email}>"