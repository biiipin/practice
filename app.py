from flask import Flask, redirect, render_template, request, url_for
from models import db
from models.user import User
from models.note import Note

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        register_user = User(name=name, email=email, password=password)
        db.session.add(register_user)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return redirect(url_for('dashboard'))
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    notes = Note.query.filter_by(user_id=1).all()
    return render_template('dashboard.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    new_note = Note(title=title, content=content, user_id=1)
    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/delete_note/<int:note_id>')
def delete_note(note_id):
    note = Note.query.get(note_id)
    if note:
        db.session.delete(note)
        db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)
