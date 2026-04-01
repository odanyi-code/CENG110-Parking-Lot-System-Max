import unittest
from src.simple_list import SimpleList

class TestSimpleList(unittest.TestCase):

    def setUp(self):
        self.lst = SimpleList()

    def test_add(self):
        self.lst.add(1)
        self.lst.add(2)
        self.assertEqual(self.lst.size(), 2)

    def test_remove(self):
        self.lst.add(1)
        self.lst.add(2)
        self.lst.remove(1)
        self.assertEqual(self.lst.size(), 1)
        self.assertEqual(self.lst.get(0), 2)

    def test_get(self):
        self.lst.add("a")
        self.lst.add("b")
        self.assertEqual(self.lst.get(0), "a")
        self.assertEqual(self.lst.get(1), "b")

    def test_is_empty(self):
        self.assertTrue(self.lst.is_empty())
        self.lst.add(1)
        self.assertFalse(self.lst.is_empty())

    def test_size(self):
        self.assertEqual(self.lst.size(), 0)
        self.lst.add(1)
        self.assertEqual(self.lst.size(), 1)
        self.lst.add(2)
        self.assertEqual(self.lst.size(), 2)

    def test_get_all(self):
        self.lst.add(1)
        self.lst.add(2)
        items = self.lst.get_all()
        self.assertEqual(items, [1, 2])
        # Ensure it's a shallow copy
        items.append(3)
        self.assertEqual(self.lst.size(), 2)

if __name__ == '__main__':
    unittest.main()
