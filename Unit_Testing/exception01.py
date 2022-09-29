import unittest

def throwe_ex(var):
    if var == 100:
        raise Exception("not a valid number")
    else:
        return True


class LearnUnitTest(unittest.TestCase):

    def test_sample01(self):
        #assertion can be used like below
        #self.assertEqual(throwe_ex(100), True)

        #instead above we can use assert raises like below
        #it is expecting the exception which means if any exception raises it will be able to handle that
        self.assertRaises(Exception, throwe_ex, 10)


if __name__ == "__main__":
    unittest.main()



