import unittest
from src.simple_list import SimpleList

class TestSimpleList(unittest.TestCase):
    """Test cases for the SimpleList class."""

    def setUp(self):
        """Set up an empty SimpleList for each test."""
        self.lst = SimpleList()

    def test_add(self):
        """Verify adding an item to the list."""
        self.lst.add(1)
        self.lst.add(2)
        self.assertEqual(self.lst.size(), 2)

    def test_remove(self):
        """Verify removing an item from the list."""
        self.lst.add(1)
        self.lst.add(2)
        self.lst.remove(1)
        self.assertEqual(self.lst.size(), 1)
        self.assertEqual(self.lst.get(0), 2)

    def test_get(self):
        """Verify getting an item from the list by index."""
        self.lst.add("a")
        self.lst.add("b")
        self.assertEqual(self.lst.get(0), "a")
        self.assertEqual(self.lst.get(1), "b")

    def test_is_empty(self):
        """Verify checking if the list is empty."""
        self.assertTrue(self.lst.is_empty())
        self.lst.add(1)
        self.assertFalse(self.lst.is_empty())

    def test_size(self):
        """Verify getting the size of the list."""
        self.assertEqual(self.lst.size(), 0)
        self.lst.add(1)
        self.assertEqual(self.lst.size(), 1)
        self.lst.add(2)
        self.assertEqual(self.lst.size(), 2)

    def test_get_all(self):
        """Verify getting all items from the list as a shallow copy."""
        self.lst.add(1)
        self.lst.add(2)
        items = self.lst.get_all()
        self.assertEqual(items, [1, 2])
        # Ensure it's a shallow copy
        items.append(3)
        self.assertEqual(self.lst.size(), 2)

if __name__ == '__main__':
    unittest.main()
