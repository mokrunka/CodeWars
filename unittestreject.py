import unittest
from reject import reject

class Test(unittest.TestCase):

    def test_reject(self):
        result = reject([1, 2, 3, 4, 5, 6], lambda x: x%2==0)
        self.assertEqual(result , [1, 3, 5])
        self.assertEqual(reject(['a', 'b', 3, 'd'], lambda x: type(x)==int), ['a', 'b', 'd']);
        self.assertEqual(reject(['a', 'b', 3, 'd'], lambda x: type(x)==str), [3]);

if __name__ == '__main__':
    unittest.main()