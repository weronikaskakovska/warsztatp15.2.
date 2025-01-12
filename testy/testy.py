import unittest
from funkcje import dod, odejm
class TestMyModule(unittest.TestCase):

    def test_dod(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_odejm(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
