import unittest

##if raises more than one type of exception

#custom exception 01
class custome_exception(Exception):
    pass

#custome exception 02
class second_custome_exception(Exception):
    pass


def throwe_ex(var):
    if var == 100:
        raise custome_exception("not a valid number")

    elif var == 200:
        raise second_custome_exception("not a valid number again")
    else:
        return True


class LearnUnitTest(unittest.TestCase):

    def test_sample01(self):

        #2 exceptions are sent via parameter
        self.assertRaises((custome_exception, second_custome_exception), throwe_ex, 200)


if __name__ == "__main__":
    unittest.main()