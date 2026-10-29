from text import Text


class Buffer:
    def __init__(self) -> None:
        self._items: list[Text] = []

    def add(self, item: Text) -> None:
        self._items.append(item)

    def extend(self, items: list[Text]) -> None:
        self._items.extend(items)

    def get_all(self) -> list[Text]:
        return self._items.copy()

    def clear(self) -> None:
        self._items.clear()

    def is_empty(self) -> bool:
        return not self._items
