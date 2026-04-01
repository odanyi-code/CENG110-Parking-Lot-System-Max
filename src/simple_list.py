class SimpleList:
    """
    A custom List-based data structure.

    We use a built-in Python list for the underlying data structure because it
    provides dynamic resizing, easy indexing, and flexible removal. This wrapper
    class encapsulates the internal list, keeping the representation hidden.
    """

    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def get(self, index):
        return self._items[index]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def get_all(self):
        return list(self._items)
