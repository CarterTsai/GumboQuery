import os
import sys
import json

# add up directory to sys for import lib
sys.path.append('../')
from lib.GetElement import GumboQuery

q = GumboQuery("http://b2b.cnyes.com/news/ochart/nav_Chart_data.aspx?code=B08,080")

dt = q.query("table > tr > td[class=dt]")
rt = q.query("table > tr > td[class=rt]")
dtData = [x.text for x in dt]
rtData = [x.text for x in rt]

allData = []

for x in xrange(len(dtData)):
    allData.extend( [{"dt": dtData[x], "rt": rtData[x]}])

text = json.dumps(allData)
with open("config.json",'w') as fo:
    fo.write(text)
