import re
import unittest


class TestRe(unittest.TestCase):
    def test_1(self):
        s = '上海易宝软件有限公司'
        r1 = s.find('软件')
        self.assertIsNot(r1, -1)
        r2 = s.find('网络')
        self.assertIs(r2, -1)



unittest.main()