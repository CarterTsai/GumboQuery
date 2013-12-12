import unittest
import sys
# add up directory to sys for import lib
sys.path.append('../')
from lib.GetElement import GumboQuery


class GumboQueryTest(unittest.TestCase):

    def setUp(self):

        self.q = GumboQuery('test.html')

    def test_query_class(self):
        x = self.q.query('.myClass')
        self.assertEqual(x[0].text, unicode('345'))

    def test_query_id(self):
        x = self.q.query('#myID')
        self.assertEqual(x[0].text, unicode('Good Idea'))

    def test_query_element(self):
        x = self.q.query('a')
        self.assertEqual(x[0].text, unicode('gg'))
        self.assertEqual(x[1].text, unicode('a link'))

        x = self.q.query('h1')
        self.assertEqual(x[0].text, unicode('123'))
        self.assertEqual(x[1].text, unicode('345'))

    def test_query_element_children(self):
        x = self.q.query('div > a')
        self.assertEqual(x[0].text, unicode('a link'))

        x = self.q.query('.tt > #jj')
        self.assertEqual(x[0].text, unicode('JOB'))

    def test_query_attrs(self):
        x = self.q.query('div[title=good]')
        self.assertEqual(x[0].text, unicode('345'))


    def test_find_id(self):
        x = self.q.findID('div', 'myID')
        self.assertEqual(x[0].text, unicode('Good Idea'))

    def test_find_title(self):
        x = self.q.findTitle('h1', 'cc')
        self.assertEqual(x[0].text, unicode('345'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GumboQueryTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
