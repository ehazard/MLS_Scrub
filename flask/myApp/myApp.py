from flask import Flask, render_template
import connect2MC as connect #connect.basetHTML()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('placeholder.html')
