import unittest
from calc import Calc

class calcClassTest(unittest.TestCase):

    ##test Add function
    def test_addFunc(self):
        add = Calc()
        self.assertEqual(add.add(10,5), 15)
        self.assertEqual(add.add(20,10), 30)

    ##test Subtract function
    def test_subtractFunc(self):
        add = Calc()
        self.assertEqual(add.subtract(10,5), 5)
        self.assertEqual(add.subtract(20,10), 10)
        self.assertEqual(add.subtract(15,3), 12)

    ##test Divide function
    def test_divideFunc(self):
        add = Calc()
        self.assertEqual(add.divide(10,5), 2)
        self.assertEqual(add.divide(20,10), 2)
        self.assertEqual(add.divide(50, 5), 10)

    ##test multiply function
    def test_multiplyFunc(self):
        add = Calc()
        self.assertEqual(add.multiply(10,5), 50)
        self.assertEqual(add.multiply(20,10), 200)
        self.assertEqual(add.multiply(50, 5), 250)

    ##test power function
    def test_powerFunc(self):
        add = Calc()
        self.assertEqual(add.power(10,2), 100)
        self.assertEqual(add.power(3,4), 81)
        self.assertEqual(add.power(2, -3), 0.125)

    ##test squareroot function
    def test_sqrtFunc(self):
        add = Calc()
        self.assertEqual(add.sqrt(81), 9)
        self.assertEqual(add.sqrt(4), 2)
        self.assertEqual(add.sqrt(10000), 100)

    ##input must be integers. Lets test that
    def test_inputs(self):
        func = Calc()
        with self.assertRaises(ValueError):
            func.add([234], 5)
            func.subtract(364, {"name":"John"})
            func.divide(352, 0)
            func.divide([748,3782,493], {"1":"2"})
            func.sqrt(-5)
            func.sqrt({0,2,3,4,5})
            func.power([4,6], [7,6])



if __name__ == "__main__":
    unittest.main(exit=False)
