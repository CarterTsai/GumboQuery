import unittest
import sys
# add up directory to sys for import lib
sys.path.append('../')
from lib.GetElement import GumboPlus


class GumboPlusTest(unittest.TestCase):

    def setUp(self):
        testHtml = '<h1 class="ss cc">123</h1>' \
                   '<div class="ss">456<div>' \
                   '<h1 class="ss" title="cc" >345</h1>' \
                   '<div class="myClass" title="good" >345</h1>' \
                   '<div id="myID" title="best" >Good Idea</h1>'
        self.data = GumboPlus(testHtml)

    def test_query_class(self):
        x = self.data.query('.myClass')
        self.assertEqual(x[0].contents[0], unicode('test123'))

    def test_query_id(self):
        x = self.data.query('#myID')
        self.assertEqual(x[0].contents[0], unicode('Good Idea'))

    def test_find_class(self):
        x = self.data.findClass('h1', 'ss')
        self.assertEqual(x[0].contents[0], unicode('123'))

    def test_find_title(self):
        x = self.data.findTitle('h1', 'cc')
        self.assertEqual(x[0].contents[0], unicode('345'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GumboPlusTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
