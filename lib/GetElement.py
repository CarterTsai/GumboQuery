import gumbo


class GumboPlus:
    def __init__(self, data):
        print "test"
        self.soup = gumbo.soup_parse(data)

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

    def findClass(self, elem, className):
        th = self.soup.findAll(elem)
        return self._findAttr(th, 'class', className)

    def findTitle(self, elem, titleName):
        th = self.soup.findAll(elem)
        return self._findAttr(th, 'title', titleName)
