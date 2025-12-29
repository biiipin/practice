from flask import flash
from models import db
from models.user import User


class UserControllers:

    @staticmethod
    def login(email, password:str)->bool:
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            return True
        flash('Invalid Data', 'error')
        return False
        
    @staticmethod
    def register(user):
        try:
            new_user=User(name=user['name'], email=user['email'], password=user['password'])
            db.session.add(new_user)
            db.sesssion.commit()
            flash('signed in successfully')
            return True
        except Exception as e:
            print(e)
            return False
    