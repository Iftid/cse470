import unittest



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        self.assertEqual(True, True)
        print("this method works fine")

    def test_something2(self):
        self.assertEqual(True, True)
        self.assertEqual(True, True)
        print("this method works fine")

    def test_something23(self):
        self.assertEqual(True, True)
        self.assertEqual(True, True)
        print("this method works fine")

    def test_something4(self):
        self.assertEqual(True, True)
        self.assertEqual(True, True)
        print("this method works fine")

    def test_something5(self):
        self.assertEqual(True, True)
        self.assertEqual(True, True)
        print("this method works fine")


if __name__ == '__main__':
    unittest.main()
