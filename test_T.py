import unittest
import myform
class Test_test_T(unittest.TestCase):
    def test_A(self):
        list_mail = ["ggg@mail.ru", "asis@ert.tyt", "werty@r.ht",  "myemail@mail.com", "toma@global.tu.ri"]

        for x in list_mail:
            self.assertTrue(myform.corEmail(x))

if __name__ == '__main__':
    unittest.main()
