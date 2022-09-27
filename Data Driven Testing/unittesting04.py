import unittest

def sum(a,b):
    return a+b

class SumTest(unittest.TestCase):
    """""
    def setUp(self):
        print("setup is called")
        self.a = 10
        self.b = 20
    def tearDown(self):
        self.a = 0
        self.b = 0
    """""
    def test_sumfunc_1(self):
        print("Test-1 called")
        #arrange
        a=10
        b=20
        #act
        result = sum(a, b)
        #assert
        self.assertEqual(result, a + 30)

    def test_sumfunc_2(self):
        print("Test-2 called")
        #arrange
        a=10
        b=20
        # act
        result = sum(a, b)
        # assert
        self.assertEqual(result, a + b)

if __name__ == "__main__":
    unittest.main()
