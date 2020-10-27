import unittest
from reject import reject


class Test(unittest.TestCase):
    # here, we create a function to test the 'reject' function from reject.py - all unit tests for this function go here
    def test_reject(self):
        self.assertEqual(reject([1, 2, 3, 4, 5, 6], lambda x: x%2==0) , [1, 3, 5])
        self.assertEqual(reject(['a', 'b', 3, 'd'], lambda x: type(x)==int), ['a', 'b', 'd']);
        self.assertEqual(reject(['a', 'b', 3, 'd'], lambda x: type(x)==str), [3]);

# this allows us to run the unittest directly from pycharm
if __name__ == '__main__':
    unittest.main()