import gumbo
import re
import urllib2
import types


class GumboQuery:
    def __init__(self, data):
        try:
            if not self._isUrl(data):
                self.setHtml(data)
        except TypeError:
            pass

    # private
    def _isUrl(self, url):
        isUrl = re.match('^http', url)
        if not isinstance(isUrl, types.NoneType):
            response = urllib2.urlopen(url)
            self.q = gumbo.soup_parse(response.read())
            return True
        else:
            return False

    def _findAttr(self, elem, attrName, attrValue):
        _attrs_node = []
        for d in elem:
            try:
                _attrs = dict(d.attrs)[attrName]
                if attrValue in _attrs:
                    _attrs_node.append(d)
            except (KeyError, AttributeError):
                pass
        return _attrs_node

    # public
    def setHtml(self, html):
        self.q = gumbo.soup_parse(html)

    def setUrl(self, url):
        return self._isUrl(url)

    def findClass(self, elem, className):
        all_elem = self.q.findAll(elem)
        return self._findAttr(all_elem, 'class', className)

    def findID(self, elem, idName):
        all_elem = self.q.findAll(elem)
        return self._findAttr(all_elem, 'id', idName)

    def findTitle(self, elem, titleName):
        all_elem = self.q.findAll(elem)
        return self._findAttr(all_elem, 'title', titleName)

    def query(self, queryString):
        elem = self.q.findAll()
        selectClass = re.findall("\.([-\w]+)", queryString)
        selectID = re.findall("\#([-\w]+)", queryString)
        selectElement = re.findall("([-\w]+)", queryString)
        result = []

        if len(selectClass) != 0:
            for e in elem:
                _tmp = self._findAttr(e, 'class', selectClass[0])
                if len(_tmp) != 0:
                    result.append(_tmp[0])
        if len(selectID) != 0:
            for e in elem:
                _tmp = self._findAttr(e, 'id', selectID[0])
                if len(_tmp) != 0:
                    result.append(_tmp[0])
        if len(selectElement) != 0:
            _tmp = self.q.findAll(selectElement[0])
            if len(_tmp) != 0:
                result = _tmp
        return result
