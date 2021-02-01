import random as r
from itertools import filterfalse
from itertools import combinations
import datetime
clubs = ['San Diego Chargers', 
     'New York Jets', 
     'Detroit Lions', 
     'Washington Redskins', 
     'Philadelphia Eagles', 
     'St Louis Rams', 
     'Minnesota Vikings', 
     'Dallas Cowboys', 
     'Houston Texans', 
     'San Francisco 49ers', 
     'Tampa Bay Bucs', 
     'Chicago Bears', 
     'Seattle Seahawks', 
     'New York Giants', 
     'Cincinnati Bengals', 
     'Cleveland Browns']
group1 = r.sample(clubs, 4)
clubs = list(filterfalse(lambda x: x in group1, clubs))
group2 = r.sample(clubs, 4)
clubs = list(filterfalse(lambda x: x in group2, clubs))
group3 = r.sample(clubs, 4)
clubs = list(filterfalse(lambda x: x in group3, clubs))
group4 = r.sample(clubs, 4)
clubs = list(filterfalse(lambda x: x in group4, clubs))
groupedList = []
groupedList.append(group1)
groupedList.append(group2)
groupedList.append(group3)
groupedList.append(group4)
date = datetime.datetime(2021, 9, 14, 0, 0)
code = date.weekday()
if code!=2:
    if code<2:
        code=12+code
    else:
        code=5+code
    date-=datetime.timedelta(days=code)
hours_=0
minutes_=0
for sample in groupedList:
    for pair in combinations(sample, 2):
        print(pair[0], ' - ', pair[1])
        hours_=r.randint(0, 23)
        minutes_=r.randint(0, 59)
        date+=datetime.timedelta(days=14, hours=hours_, minutes=minutes_)
        print(date.strftime('%d/%m/%y, %H:%M'))
        date-=datetime.timedelta(hours=hours_, minutes=minutes_)
input("Press Enter to continue...")