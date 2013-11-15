import gumbo


class GumboPlus:
    def __init__(self, data):
        print "test"
        self.soup = gumbo.soup_parse(data)

    def _findAttr(self, elem, attrName, attrValue):
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
        all_elem = self.soup.findAll(elem)
        return self._findAttr(all_elem, 'class', className)

    def findTitle(self, elem, titleName):
        all_elem = self.soup.findAll(elem)
        return self._findAttr(all_elem, 'title', titleName)
