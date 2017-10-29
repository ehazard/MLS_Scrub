import urllib, calendar
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
    mConv = dict(March=3,April=4,May=5,June=6,July=7,August=8,September=9,October=10)
    temp = []
    for i in matchDates:
        string = i.contents[0] # Friday, January 1 2017
        string = string.split(' ', 1) # ['Friday,' 'January 1 2017']
        date = string[1].split(' ') # January 1 2017 -- [0][1][2]
        dString = date[2] + "-" + str(mConv[date[0]]) + "-" + date[1].replace(",","")
        temp.append(dString)
    return temp

def homeTeam(soup):
    ## Get the other team's name
    oTeam = soup.findAll("div", {"class": "match_matchup"})
    oTeams_A = []
    for j in oTeam:
        on_hand = str(j.contents[0].lower().replace("at ", ""))
        if on_hand == "fc dallas": #FC Dallas is special because "fc dallas" is in their URL
            on_hand = on_hand.replace("sc","").rstrip().replace(" ", "-")
        else:
            on_hand = on_hand.replace("fc","").rstrip().replace("sc","").replace(".","").replace(" ", "-")
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


## Main
# dateTime(YYYY-MM-DD) + HomeTeam + AwayTeam + /recap  ------> 2017-10-25-chicago-fire-vs-new-york-red-bulls/
soup = baseHTML()
MDs = matchDates(soup)
homeOaway = homeTeam(soup)
