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
    dates.append(date[0])
#dates are now in dates[]

temp = 0
opp = []
for i in array:
    m = str(i).partition('2017/')
    k = str(m[2]).partition('match-recap-')
    newStr = k[2].replace("portland-timbers","").replace("-","")
    newStr = newStr.translate(None, digits)
    opp.append(newStr)
#opponents are now listed (by date) in op[]
