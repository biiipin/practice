import os
from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate
from controllers.note_controller import NoteController
from controllers.user_controller import UserControllers
from models import db
from models.db import db_config

app = Flask(__name__)
app.secret_key= os.getenv('APP_SECRET_KEY')


app.config['SQLALCHEMY_DATABASE_URI']=db_config
db.init_app(app)


migrate=Migrate(app,db)
UserController= UserControllers()

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
   recent_notes = NoteController.get_recent_notes(limit=3)
   return render_template('home.html', notes=recent_notes)

@app.route('/addnote', methods=['GET'])
def add_note():
    return render_template('add_note.html')

@app.route('/addnote_form', methods=['POST'])
def addnote_form():
    title=request.form.get('title')
    content=request.form.get('content')
    NoteController.create_note(title=title, content=content) 
    return redirect(url_for('home'))

@app.route('/seenotes', methods=['GET'])
def see_notes():
    return render_template('see_notes.html')

@app.route('/register', methods=['POST'])
def register():
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        register_user = UserControllers().register({'name':name, 'email':email, 'password':password})
        if register_user:
            return redirect(url_for('dashboard'))
        return redirect(url_for('signup'))

@app.route('/login', methods=['POST'])
def login():
    email=request.form['email']
    password=request.form['password']
    valid_user=UserControllers().login(email=email, password=password)
    if valid_user:
        return redirect(url_for('dashboard'))
    return redirect(url_for('signin'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)
