import unittest
import main


class MainTest(unittest.TestCase):
    def test_helloworld(self):
        ret = main.helloworld("TEST")
        self.assertEqual(ret, "Hello World! Denial")


if __name__ == "__main__":
    unittest.main()
