import connect2MC as connect #connect.basetHTML()
import json

jsonF = open('teams.json').read()
newDict = json.loads(jsonF) #newDict['SEA']

sea = newDict['RSL']
print str(connect.baseHTML(sea, "RSL"))
