# MLS Match Center README

The original idea was to route the queries through the specific club matchenters (matchcenter.timbers.com) but after comparing the different match centers (minnesota vs. timbers), it became obvious that the different DB managers were using their own syntax for the URLs. This in turn led to making the queries follow the MLS match center. The idea is something like this:

1. Choose team you want to know more about
2. Find that team's schedule
3. Use the team's schedule to create the MLSSoccer.com matchcenter URLs
4. make query on the URLs

MLS Match center uses the same syntax across the board:

https://matchcenter.mlssoccer.com/matchcenter/ + dateTime(YYYY-MM-DD) + HomeTeam + AwayTeam + /recap
