from flask import Flask, render_template,request,url_for
import json, os
import connect2MC as connect #connect.basetHTML()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    team = "No Team Selected...go choose one dumby"
    if request.method == 'POST':
        team = request.form['teamN']
        return render_template('placeholder.html', team=team)
    return render_template('placeholder.html', team=team)

@app.route('/subs', methods=['GET', 'POST'])
def subs_stats():
    if request.method == 'POST':
        team = request.form['teamN']
        filename = os.path.join(app.static_folder, 'teams.json')
        with open(filename) as jsonFile:
            newDict = json.load(jsonFile)
        subList = connect.baseHTML(newDict["teamURL"][team], team, newDict["teamCodes"][team], newDict["teamPics"][team])
        return render_template('placeholder.html', team=team, subList=subList)
