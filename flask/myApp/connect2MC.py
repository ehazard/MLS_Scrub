import urllib, calendar, urllib2
from bs4 import BeautifulSoup

def baseHTML(url, teamN, teamURL_code, TPS):
    global teamCode, teamPic_S, t
    teamCode = teamN
    t = teamURL_code
    teamPic_S = TPS
    gross = urllib.urlopen(url)
    lol = gross.read()
    soup = BeautifulSoup(lol, "html.parser")
    try:
        dates = matchDates(soup)
        homeT = homeTeam(soup)
    except:
        print "Error on matchDates() or homeTeam()"
    try:
        URLs = makeURLs(dates,homeT)
    except:
        print "Error on URL making and sub finding"
    superCal = subs(URLs)
    return superCal

def matchDates(soup):
    matchDates = soup.findAll("div", { "class": "match_date"})
    mConv = dict(March='03',April='04',May='05',June='06',July='07',August='08',September='09',October='10')
    temp = []
    for i in matchDates:
        string = i.contents[0] # Friday, January 1 2017
        string = string.split(' ', 1) # ['Friday,' 'January 1 2017']
        date = string[1].split(' ') # January 1 2017 -- [0][1][2]
        day = date[1].replace(",","")
        if int(day)<10:
            day = '0' + date[1].replace(",","")
        dString = date[2] + "-" + str(mConv[date[0]]) + "-" + day + "-"
        temp.append(dString)
    return temp

def homeTeam(soup):
    ## Get the other team's name
    oTeam = soup.findAll("div", {"class": "match_matchup"})
    oTeams_A = []
    for j in oTeam:
        on_hand = str(j.contents[0].lower().replace("at ", "").replace(".","").replace(" ", "-")).rstrip()
        if on_hand == "orlando-city":
            on_hand = "orlando-city-sc"
        elif on_hand == "columbus-crew":
            on_hand = "columbus-crew-sc"
        elif on_hand == "montreal":
            on_hand = "montreal-impact"
        oTeams_A.append(on_hand)
    ## Decide if the game is home or away
    hORa = soup.findAll("span", { "class": "match_home_away"})
    temp_A = []
    indx = 0
    for i in hORa:
        if i.contents[0] == 'H':
            team = t + "-vs-" + oTeams_A[indx]
            indx += 1
        else:
            team = oTeams_A[indx] +  "-vs-" + t
            indx += 1
        temp_A.append(team)
    return temp_A

def makeURLs(MDs, homeOaway):
    indx, preface = 0, "https://matchcenter.mlssoccer.com/matchcenter/"
    temp_L = []
    while indx < len(MDs):
        temp_L.append(preface + MDs[indx] + homeOaway[indx] + "/feed")
        indx += 1
    return temp_L

def subs(URLs):
    subs = []
    for i in URLs:
        url = i
        grossHTML = urllib.urlopen(url)
        allHTML = grossHTML.read()
        soup = BeautifulSoup(allHTML, "html.parser")
        allButtons = soup.findAll("table", { "class": "bx-subs bx-table"})[0].findAll('tr')
        subN = 0
        for i in allButtons:
            src = i.find('img')['src']
            if src == teamPic_S:
                subN += 1
        subs.append(subN)
    return subs
