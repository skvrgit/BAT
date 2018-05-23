import unittest
import test

class TestAnalyze(unittest.TestCase):

    def test_analyze(self):
        pattern = "ERROR|WARN"

        self.assertEqual("", test.filter("", pattern))

        self.assertEqual("", test.filter("INFO", pattern))

        self.assertEqual("ERROR", test.filter("ERROR", pattern))

        self.assertEqual("WARN", test.filter("WARN", pattern))

        self.assertEqual("2018/01/01 00:00:00.000000 [ERROR] xxx", \
                         test.filter("2018/01/01 00:00:00.000000 [ERROR] xxx", pattern))

        self.assertEqual("2018/01/01 11:11:11.111111 [ERROR] yyy", \
                         test.filter("2018/01/01 00:00:00.000000 [INFO] xxx\n2018/01/01 11:11:11.111111 [ERROR] yyy", pattern ))

        self.assertEqual("2018/01/01 00:00:00.000000 [ERROR] xxx\n2018/01/01 11:11:11.111111 [ERROR] xxx",\
                         test.filter("2018/01/01 00:00:00.000000 [ERROR] xxx\n2018/01/01 11:11:11.111111 [ERROR] xxx", pattern))




if __name__ == "__main__":
    unittest.main()
