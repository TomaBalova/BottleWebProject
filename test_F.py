import unittest
import myform
class Test_test_F(unittest.TestCase):
    def test_A(self):
        list_mail = [" ", "@@", "1", "1@", "mail.@", "ggg@mail.u", "ex,mple", "rtty.rtty@gm", "asis@ert|tyt", "werty@r...h", "=we@tr.hh", "myemail@mail@com", "...", "Toma\\Balova\"Sh@g.go", "6t5t@33.44", "345erity@ghj.34@gof", "-_-tt=_=@hoy.hoy.ho"]
        for x in list_mail:
            self.assertFalse(myform.corEmail(x))

if __name__ == '__main__':
    unittest.main()
