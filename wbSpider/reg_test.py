#正则表达式测试

import unittest
import re

class TestReg(unittest.TestCase):

    #分组
    def test_group(self):
        content = "10月12日0-24时，四川无新增新型冠状病毒肺炎确诊病例，新增治愈出院病例2例，无新增疑似病例，无新增死亡病例。" \
                  "截至10月12日24时，全省累计报告新型冠状病毒肺炎确诊病例1214例（其中境外输入652例），累计治愈出院1199例，" \
                  "死亡3例，目前在院隔离治疗12例，28人尚在接受医学观察。10月12日0-24时，全省无新增无症状感染者，当日转为确诊病例0例，" \
                  "当日解除集中隔离医学观察0例，尚在集中隔离医学观察6例。截至10月12日24时，全省均为低风险区。"

        #提取出确诊数、治愈数、死亡数,一个()为一个group, .*表示0个或者多个除了\r \n的单个字符，？表示非贪婪模式匹配。
        pattern = "确诊病例(\d+)例.*?治愈出院(\d+)例.*?死亡(\d+)例"
        res = re.search(pattern, content)
        print(res)
        #确诊数，第1个()
        print(res.group(1))
        # 治愈数，第2个()
        print(res.group(2))
        # 死亡数，第3个()
        print(res.group(3))




    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
