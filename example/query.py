import sys
# add up directory to sys for import lib
sys.path.append('../')
from lib.GetElement import GumboQuery

q = GumboQuery(open('../test.html').read())

data = q.query(".nba-stat-type-15")

