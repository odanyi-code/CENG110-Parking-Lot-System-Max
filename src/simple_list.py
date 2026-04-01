class SimpleList:
    """
    A custom List-based data structure.

    A built-in Python list is chosen because it provides dynamic resizing,
    easy indexing, and flexible removal. This wrapper encapsulates the internal
    list to keep its representation hidden.
    """

    def __init__(self):
        """Initializes an empty custom list."""
        self._items = []

    def add(self, item):
        """Adds an item to the end of the list."""
        self._items.append(item)

    def remove(self, item):
        """Removes the first occurrence of the item from the list."""
        self._items.remove(item)

    def get(self, index):
        """Retrieves an item at the specified index."""
        return self._items[index]

    def is_empty(self):
        """Checks if the list is empty."""
        return len(self._items) == 0

    def size(self):
        """Returns the number of items in the list."""
        return len(self._items)

    def get_all(self):
        """Returns a shallow copy of the list for iteration."""
        return list(self._items)
