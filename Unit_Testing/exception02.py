import unittest

##making custom exception
class custome_exception(Exception):
    pass


def throwe_ex(var):
    if var == 100:
        v1 = 12/0
        #here i am raising my exception over here
        raise custome_exception("not a valid number")
    else:
        return True


class LearnUnitTest(unittest.TestCase):

    def test_sample01(self):

        self.assertRaises(custome_exception, throwe_ex, 100)


if __name__ == "__main__":
    unittest.main()