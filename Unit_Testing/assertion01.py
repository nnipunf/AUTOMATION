"""""
import unittest

class Test():
    pass

class Test1():
    pass

class LearnUnitTest(unittest.TestCase):

    def test_sample01(self):


        #a = 1
        #b = 1
        #self.assertEqual(a, b, msg="assumption is failed")
        #self.assertNotEqual(a,b)

        T1 = Test()
        T2 = Test()


        self.assertIs(T1, T2)


if __name__ == "__main__":
    unittest.main()
"""