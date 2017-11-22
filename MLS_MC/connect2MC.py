import urllib, calendar, urllib2
from bs4 import BeautifulSoup

def baseHTML():
    # https://www.mnufc.com/schedule?month=all&year=2017&club_options=11&op=Update&form_build_id=form-QFfw1zYcA-WipqkQzW_mmLoPMN0_IJiJkUL4TwkDVM0&form_id=mp7_schedule_hub_search_filters_form
    # https://www.timbers.com/schedule?month=all&year=2017&club_options=7&op=Update&form_build_id=form-ztMv4lNCHH_kAAjTbGPY6E2NykGGbBKZyJ-r1d1_0f4&form_id=mp7_schedule_hub_search_filters_form
    url = "https://www.timbers.com/schedule?month=all&year=2017&club_options=7&op=Update&form_build_id=form-ztMv4lNCHH_kAAjTbGPY6E2NykGGbBKZyJ-r1d1_0f4&form_id=mp7_schedule_hub_search_filters_form"
    gross = urllib.urlopen(url)
    lol = gross.read()
    soup = BeautifulSoup(lol, "html.parser") #HTML of the above web page is now in *soup*
    return soup

def matchDates(soup):
    matchDates = soup.findAll("div", { "class": "match_date"})
    mConv = dict(March='03',April='04',May='05',June='06',July='07',August='08',September='09',October='10')
    #mNum = dict()
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
    #TO_DO: Clean this if/elif/else crap up
    for j in oTeam:
        on_hand = str(j.contents[0].lower().replace("at ", "").replace(".","").replace(" ", "-")).rstrip()
        oTeams_A.append(on_hand)
    ## Get who's home
    hORa = soup.findAll("span", { "class": "match_home_away"})
    temp_A = []
    indx = 0
    for i in hORa:
        if i.contents[0] == 'H':
            team = "portland-timbers" + "-vs-" + oTeams_A[indx]
            indx += 1
        else:
            team = oTeams_A[indx] +  "-vs-" + "portland-timbers"
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
            if src == "https://img.mlsdigital.net/www.mlssoccer.com/7/image/207523/x50.png":
                subN += 1
        subs.append(subN)
    return subs
## Main
# dateTime(YYYY-MM-DD) + HomeTeam + AwayTeam + /recap  ------> 2017-10-25-chicago-fire-vs-new-york-red-bulls/recap
soup = baseHTML()
MDs = matchDates(soup)
homeOaway = homeTeam(soup)
URLs = makeURLs(MDs,homeOaway)
#subs = subs(URLs)
print URLs
