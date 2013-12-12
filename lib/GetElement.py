import gumbo
import re
import urllib2
import types
import BeautifulSoup


class GumboQuery:
    def __init__(self, data):
        try:
            if not self._isUrl(data):
                if not self._isFile(data):
                    self.setHtml(data)
            self._allElem = self.q.findAll()
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

    def _isFile(self, filename):
        isFile = re.match('[\w]+.html', filename)
        if not isinstance(isFile, types.NoneType):
            content = open(filename)
            self.q = gumbo.soup_parse(content.read())
            return True
        else:
            return False

    def _findElemAttr(self, elem, attrName, attrValue):
        _attrs_node = []

        if elem.__class__ == BeautifulSoup.NavigableString:
                elem = elem.parent
        try:
            _attrs = dict(elem.attrs)[attrName]
            if attrValue in _attrs:
                _attrs_node.append(elem)
        except (KeyError, AttributeError):
            pass

        return _attrs_node

    def _findAttr(self, elem, attrName, attrValue):
        _attrs_node = []

        for d in elem:
            if d.__class__ == BeautifulSoup.NavigableString:
                d = d.parent
            try:
                _attrs = dict(d.attrs)[attrName]
                if attrValue in _attrs:
                    _attrs_node.append(d)
            except (KeyError, AttributeError):
                pass

        return _attrs_node

    def _selector(self, q, selectType, elemName):
        result = []
        if selectType == 'id' or selectType == 'class':
            elem = self._allElem
            for e in elem:
                _tmp = self._findAttr(e, selectType, elemName)
                if len(_tmp) != 0:
                    result.append(_tmp[0])
        elif selectType == 'attrs':
            attrs = list(re.findall("(\w+)\[(\w+)(\W+)+([-\w]+)\]", elemName)[0])
            elem = attrs[0]
            attrs_name = attrs[1]
            selectors = attrs[2]
            val = attrs[3]
            _tmp = []

            main_elem = q.findAll(elem)


            if selectors == '=':
                for e in main_elem:
                    _findNode = self._findElemAttr(e, attrs_name, val)
                    if len(_findNode) != 0:
                        _tmp.append(_findNode[0])
            elif selectors == '~=':
                pass
            elif selectors == '|=':
                pass
            result = _tmp
        else:
            elem = q.findAll(elemName)
            if len(elem) != 0:
                result = elem

        return result

    def _parseType(self, queryString):
        if re.findall("\.([-\w]+)", queryString):
            return ['class', queryString[1:]]
        elif re.findall("\#([-\w]+)", queryString):
            return ['id', queryString[1:]]
        elif re.findall("[\w]+\[[\w]+[~|]?=[-\w]+\]", queryString):
            return ['attrs', queryString]
        else:
            return ['elem', queryString]

    # public
    def setHtml(self, html):
        self.q = gumbo.soup_parse(html)

    def setUrl(self, url):
        return self._isUrl(url)

    def setFile(self, filename):
        return self._isFile(filename)

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
        qData = []
        _next = ''

        for selector in queryString.split():
            if selector == '>':
                _next = 'child'
            else:
                sType = self._parseType(selector)
                if _next != 'child':
                    _subData = self._selector(self.q, sType[0], sType[1])
                    for _d in _subData:
                        qData.append(_d)
                else:
                    _tmp = qData
                    qData = []
                    for _childElement in _tmp:
                        _subData = self._selector(_childElement, sType[0], sType[1])
                        for _d in _subData:
                            qData.append(_d)

        return qData
