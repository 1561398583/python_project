import unittest
import json

class Test1(unittest.TestCase):

    def test_json(self):
        data = [10, 20, 30, 1, 2, 3]
        jd = json.dumps(data)
        print(jd)

    def test_list(self):
        data = [0]*6
        for i in range(0, 6):
            data[i] = 100 + i
        jd = json.dumps(data)
        print(jd)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()