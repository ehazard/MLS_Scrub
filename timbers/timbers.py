import urllib, re
from BeautifulSoup import BeautifulSoup
from string import digits


url = "https://www.timbers.com/schedule?month=all&year=2017&club_options=7&op=Update&form_build_id=form-ztMv4lNCHH_kAAjTbGPY6E2NykGGbBKZyJ-r1d1_0f4&form_id=mp7_schedule_hub_search_filters_form"
gross = urllib.urlopen(url)
lol = gross.read()

soup = BeautifulSoup(lol)

allButtons = soup.findAll("a", { "class": "button match-link-2 button-secondary"})
array = []
dates = []
timberMC = "https://matchcenter.timbers.com/matchcenter/2017"
# We need to create an individual link for each match, that looks like this:
#        https://matchcenter.timbers.com/matchcenter/2017-08-23-portland-timbers-vs-colorado-rapids/feed
itera = 0
for link in allButtons:
    try:
        string = str((link.get('href')))
        array.append(string)
        itera += 1
    except IndexError:
        print "Error"

#--------
# Get all the dates
#-------
temp = 0
dates = []
for i in array:
    m = str(i).partition('2017/')
    if temp == 0:
        date = m[2].partition('/recap')
    else:
        date = m[2].partition('/match')
    temp += 1
    date = list(date[0])
    date[2] = '-'
    fDate = ''.join(date)
    fDate = "-" + fDate + "-"
    dates.append(fDate)
#dates are now in dates[]

temp = 0
opp = []
for i in array:
    m = str(i).partition('2017/')
    k = str(m[2]).partition('recap-')
    loc = re.search("\d", str(k[2]))
    sLoc = loc.start()
    k = list(k[2])
    k[sLoc] = 'vs'
    k = k[:-2]
    newString = ''.join(k)
    opp.append(newString)
#opponents are now listed (by date) in opp[]

fURL = []
## combining both manips to create new url
if len(opp) == len(dates):
    length = len(opp)
    for i in range(0,length):
        if dates[i] == "-05-20-":
            temp = timberMC + dates[i] + "montreal-impact-vs-portland-timbers/feed"
        else:
            temp = timberMC + dates[i] + opp[i] + "/feed"
        fURL.append(temp)
else:
    print "There was a problem"
## now each final URL is found in fURL[]

subs = []
for i in fURL:
    url = i
    grossHTML = urllib.urlopen(url)
    allHTML = grossHTML.read()
    soup = BeautifulSoup(allHTML)
    allButtons = soup.findAll("table", { "class": "bx-subs bx-table"})[0].findAll('tr')
    subN = 0
    for i in allButtons:
        src = i.find('img')['src']
        if src == "https://img.mlsdigital.net/www.mlssoccer.com/7/image/207523/x50.png":
            subN += 1
    subs.append(subN)
## the ammount of subs per game is now listed in subs[]

indx = 0
for i in subs:
    print str(opp[indx]) + " : " +  str(i)
    indx += 1
