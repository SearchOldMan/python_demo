import unittest,mytest

class ProductCase(unittest.TestCase):
    def testInt(self):
        for x in xrange(-10,20):
            for y in xrange(-10,20):
                p = mytest.test(x,y)
                self.failUnless(p==x*y,'Integer mul fail')

    def testFloat(self):
        for x in xrange(-10,20):
            for y in xrange(-10,20):
                x = x/10.0
                y = y/10.0
                p = mytest.test(x,y)
                self.failUnless(p==x*y,'Integer mul fail')

if __name__ == '__main__':
    unittest.main()