from flask import Flask, render_template,request
import json
import connect2MC as connect #connect.basetHTML()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    team = "Yo"
    if request.method == 'POST':
        team = request.form['teamN']
        return render_template('placeholder.html', team=team)
    return render_template('placeholder.html', team=team)

@app.route('/subs', methods=['GET', 'POST'])
def subs_stats():
    if request.method == 'POST':
        team = request.form['teamN']
        jsonF = open('teams.json').read()
        newDict = json.loads(jsonF) #newDict['SEA']
        return str(connect.baseHTML(newDict[team]))
        #return render_template('placeholder.html', team=team)
