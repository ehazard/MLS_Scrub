import urllib
from bs4 import BeautifulSoup

url = "https://www.timbers.com/schedule?month=all&year=2017&club_options=7&op=Update&form_build_id=form-ztMv4lNCHH_kAAjTbGPY6E2NykGGbBKZyJ-r1d1_0f4&form_id=mp7_schedule_hub_search_filters_form"
gross = urllib.urlopen(url)
lol = gross.read()

soup = BeautifulSoup(lol, "html.parser") #HTML of the above web page is now in *soup*

matchDates = soup.findAll("div", { "class": "match_date"})

for i in matchDates:
    print i
