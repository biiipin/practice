import flask as Flask, render_template


app=Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')