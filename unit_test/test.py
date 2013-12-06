import unittest
import sys
# add up directory to sys for import lib
sys.path.append('../')
from lib.GetElement import GumboQuery

class GumboQueryTest(unittest.TestCase):

    def setUp(self):
        testHtml = '<h1 class="ss cc">123</h1>' \
                   '<div class="ss">456</div>' \
                   '<a> gg </a>'\
                   '<h1 class="gg" title="cc" >345</h1>' \
                   '<div class="myClass" title="good" >345</div>' \
                   '<div id="myID" title="best" >Good Idea</div>' \
                   '<div><a href="#">a link</a></div>' \
                   '<div class="tt"><div id="jj">JOB</div></div>'
        self.q = GumboQuery(testHtml)

    def test_query_class(self):
        x = self.q.query('.myClass')
        self.assertEqual(x[0].contents[0], unicode('345'))

    def test_query_id(self):
        x = self.q.query('#myID')
        self.assertEqual(x[0].contents[0], unicode('Good Idea'))

    def test_query_element(self):
        x = self.q.query('a')
        self.assertEqual(x[0].contents[0], unicode(' gg '))
        self.assertEqual(x[1].contents[0], unicode('a link'))

        x = self.q.query('h1')
        self.assertEqual(x[0].contents[0], unicode('123'))
        self.assertEqual(x[1].contents[0], unicode('345'))

    def test_query_element_children(self):
        x = self.q.query('div > a')
        self.assertEqual(x[0].contents[0], unicode('a link'))

        x = self.q.query('.tt > #jj')
        self.assertEqual(x[0].contents[0], unicode('JOB'))

    def test_find_class(self):
        x = self.q.findClass('h1', 'ss')
        self.assertEqual(x[0].contents[0], unicode('123'))

    def test_find_id(self):
        x = self.q.findID('div', 'myID')
        self.assertEqual(x[0].contents[0], unicode('Good Idea'))
    def test_find_title(self):
        x = self.q.findTitle('h1', 'cc')
        self.assertEqual(x[0].contents[0], unicode('345'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GumboQueryTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
