import unittest

class SimplisticTest(unittest.TestCase):

    def test(self):
        a = 'a'
        b = 'a'
        self.assertEqual(a, b)
    
    def test_hola(self):
        a = 'hola'
        b = 'hola'
        self.assertEqual(a, b)
        
if __name__ == '__main__':
    unittest.main()
