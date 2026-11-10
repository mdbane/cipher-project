from text import Text


class Buffer:
    """In-memory list of Text objects kept while the program is running."""

    def __init__(self) -> None:
        self._items: list[Text] = []

    def add(self, item: Text) -> None:
        """Add a Text object to the buffer."""
        self._items.append(item)

    def extend(self, items: list[Text]) -> None:
        """Add multiple Text objects to the buffer, keeping their order."""
        self._items.extend(items)

    def get_all(self) -> list[Text]:
        """Return a copy of all Text objects in the buffer."""
        return self._items.copy()

    def clear(self) -> None:
        """Remove all Text objects from the buffer."""
        self._items.clear()

    def is_empty(self) -> bool:
        """Return True if the buffer has no Text objects, False otherwise."""
        return not self._items
