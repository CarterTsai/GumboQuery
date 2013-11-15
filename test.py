from lib.GetElement import GumboPlus


html = open('test.html')

parse = GumboPlus("<h1> 123 </h1>");

#soup = gumbo.soup_parse(html.read())

#th = soup.findAll('th')

def _findAttr(elem, attrName, attrValue):
    _attrs_node = []
    for d in elem:
        try:
            _attrs = dict(d.attrs)[attrName]
            if attrValue in _attrs:
               _attrs_node.append(d)
        except KeyError:
            pass
    return _attrs_node

def findClass(elem, className):
    th = soup.findAll(elem)
    return _findAttr(th, 'class', className)

def findTitle(elem, titleName):
    th = soup.findAll(elem)
    return _findAttr(th, 'title', titleName)


#print findTitle('td', 'Minutes Played')
#classNode = findClass("nba-stat-type")

#for d in classNode:
#    print d.contents
