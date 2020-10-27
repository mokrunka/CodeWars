import unittest
from movingaverage import moving_average


class Test(unittest.TestCase):
    # here, we create a function to test the 'moving_average' function from movingaverage.py
    # - all unit tests for this function go here
    def test_moving_avg(self):
        self.assertEqual(moving_average([40, 30, 50, 46, 39, 44], 3), [40.0, 42.0, 45.0, 43.0])
        self.assertEqual(moving_average([40, 30, 50, 46, 39, 44], 2), [35.0, 40.0, 48.0, 42.5, 41.5])
        self.assertEqual(moving_average([40, 30, 50, 46, 39, 44], 4), [41.5, 41.25, 44.75])
        self.assertEqual(moving_average([40, 30, 50, 46, 39, 44], 0), None)

# this allows us to run the unittest directly from pycharm
if __name__ == '__main__':
    unittest.main()