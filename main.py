from flask import *

app = Flask(__name__)
app.secret_key = "super_secret31415926535"


@app.route('/')
def main_page():
    return render_template('main_page.html')
