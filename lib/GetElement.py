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

    def _selector(self, selectType, elemName):
        result = []
        if selectType != 'elem':
            elem = self.q.findAll()
            for e in elem:
                _tmp = self._findAttr(e, selectType, elemName)
                if len(_tmp) != 0:
                    result.append(_tmp[0])
        else:
            elem = self.q.findAll(elemName)
            if len(elem) != 0:
                result = elem

        return result

    def _parseType(self, queryString):
        if re.findall("\.([-\w]+)", queryString):
            return ['class', queryString[1:]]
        elif re.findall("\#([-\w]+)", queryString):
            return ['id', queryString[1:]]
        else:
            return ['elem', queryString]

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
        sType = self._parseType(queryString)
        return self._selector(sType[0], sType[1])
